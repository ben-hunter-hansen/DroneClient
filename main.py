import pygame
import time
import os
import json

from helpers import *
from client import *



class Window:
    def __init__(self, dimensions):
        self.xy = dimensions
        pygame.init()
        self.screen = pygame.display.set_mode(self.xy)
        self.movement = Movement.Stop()
        self.exit = False
        self.icons = []

    def hande_event(self,event):
        if event.type == pygame.KEYDOWN:
            self.movement = self.get_movement(event.key)
        elif event.type == pygame.KEYUP:
            self.movement = Movement.Stop()
        elif event.type == pygame.QUIT:
            self.exit = True

    def get_movement(self,key):
        movement = Movement.Stop() #enabled by default
        if key == pygame.K_w:
            movement = Movement.Forward()
        elif key == pygame.K_s:
            movement = Movement.Reverse()
        elif key == pygame.K_a:
            movement = Movement.Left()
        elif key == pygame.K_d:
            movement = Movement.Right()
        return movement

    def draw_hud(self):
        DrawUtils.RenderControls(self.screen,Color.Red(),Shapes.Controls(),2,pygame.draw.polygon)
        DrawUtils.RenderIcons(self.screen,self.icons,(75,25),250)


    def data_recv(self,reply):

        self.screen.fill((50,50,50))
        data = json.loads(reply)

        movements = Movement.All()
        shapes = Shapes.Controls()
        index = 0
        for m in movements:
            if self.movement == m:
                pygame.draw.polygon(self.screen,Color.Blue(),shapes[index],0)
            index += 1
        
        replyFont = pygame.font.SysFont("monospace", 16)
        mov_label = replyFont.render(data['movement'],1,Color.Blue())
        bat_label = replyFont.render(data['battery'],1,Color.Blue())
        net_label = replyFont.render(data['network'],1,Color.Blue())

        self.screen.blit(mov_label,(140,40))
        self.screen.blit(bat_label,(390,40))
        self.screen.blit(net_label,(640,40))

    def load_icons(self):
        icon_paths = Resource.Icons()
        for i in icon_paths:
            icon = pygame.image.load(os.path.join(i))
            icon.convert()
            self.icons.append(icon)

    def should_exit(self):
        return self.exit

def main():

    window = Window((800,600))
    window.load_icons()

    arduino = ArduinoClient(Network.Arduino())
    arduino.apply_on_recv(window.data_recv)

    done = False
    while not done:
        for event in pygame.event.get():
            window.hande_event(event)
        arduino.send(window.movement)
        window.draw_hud()
        pygame.display.flip()
        done = window.should_exit()


 main()
