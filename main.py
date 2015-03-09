import pygame
import time

from helpers import *
from client import *



class Window:
    def __init__(self, dimensions):
        self.xy = dimensions
        pygame.init()
        self.screen = pygame.display.set_mode(self.xy)
        self.movement = Movement.Stop()
        self.exit = False

    def hande_event(self,event):
        if event.type == pygame.KEYDOWN:
            self.movement = self.get_movement(event.key)
        elif event.type == pygame.KEYUP:
            self.movement = Movement.Stop()
        elif event.type == pygame.QUIT:
            self.exit = True

    def get_movement(self,key):
        movement = None
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
        shapes = Shapes.All()
        for shape in shapes:
            pygame.draw.polygon(self.screen,Color.Red(),shape,2)

    def data_recv(self,reply):
        self.screen.fill((0,0,0))

        movements = Movement.All()
        shapes = Shapes.All()
        index = 0
        for m in movements:
            if self.movement == m:
                pygame.draw.polygon(self.screen,Color.Blue(),shapes[index],0)
            index += 1
        #print reply

    def should_exit(self):
        return self.exit

def main():

    window = Window((800,600))
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
main();

