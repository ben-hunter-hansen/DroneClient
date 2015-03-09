import threading
import pygame

from client import *
from helpers import *

class Window (threading.Thread):
    def __init__(self, dimensions):
        threading.Thread.__init__(self)
        self.xy = dimensions
        pygame.init()
        self.screen = pygame.display.set_mode(self.xy)
        self.running = True
        self.arduino = None

    def attach(self,arduino):
    	self.arduino = arduino

    def run(self):
        while self.running:
                self.draw_components()
            	self.handle_events(self.render)
            	pygame.display.flip()

    def handle_events(self,draw_func):
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			self.quit()
    		elif event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_w:
    				response = self.arduino.move(Movement.Forward())
    				draw_func(response,Movement.Forward())
    			elif event.key == pygame.K_a:
    				response = self.arduino.move(Movement.Left())
    				draw_func(response, Movement.Left())
    			elif event.key == pygame.K_s:
    				response = self.arduino.move(Movement.Reverse())
    				draw_func(response, Movement.Reverse())
    			elif event.key == pygame.K_d:
    				response = self.arduino.move(Movement.Right())
    				draw_func(response, Movement.Right())
    		elif event.type == pygame.KEYUP:
    			response = self.arduino.move(Movement.Stop())
    			draw_func(response, Movement.Stop())

    def draw_components(self):
        pygame.draw.polygon(self.screen,Color.Red(),Shapes.ArrowUp(),2)
        pygame.draw.polygon(self.screen,Color.Red(),Shapes.ArrowLeft(),2)
        pygame.draw.polygon(self.screen,Color.Red(),Shapes.ArrowRight(),2)
        pygame.draw.polygon(self.screen,Color.Red(),Shapes.ArrowDown(),2)
        pygame.draw.polygon(self.screen,Color.Red(),Shapes.Square(),2)

    def render(self,msg, movement):
    	self.screen.fill((0,0,0))
    	if movement is Movement.Forward():
    		pygame.draw.polygon(self.screen,Color.Blue(),Shapes.ArrowUp(),0)
        elif movement is Movement.Left():
            pygame.draw.polygon(self.screen,Color.Blue(), Shapes.ArrowLeft(),0)
        elif movement is Movement.Reverse():
            pygame.draw.polygon(self.screen,Color.Blue(), Shapes.ArrowDown(),0)
        elif movement is Movement.Right():
            pygame.draw.polygon(self.screen,Color.Blue(), Shapes.ArrowRight(),0)
    	else:
    		pygame.draw.polygon(self.screen, Color.Blue(),Shapes.Square(), 0)
    	print msg
    def quit(self):
    	if self.running:
    		self.running = False


def main():

	# Create the window
	gui = Window((800,600))
	
	# Set up arduino client
	arduino = ArduinoClient(('192.168.1.21',10000))

	# Inject arduino client if connection succeeds
	if arduino.is_alive() is not None:
		print "Connection establised, starting GUI thread."
		gui.attach(arduino)
		gui.start()

main();

