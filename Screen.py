import pygame
from pygame.constants import QUIT # Import pygame to python

pygame.init() # initialtion of pygame
screen = pygame.display.set_mode((900, 450)) # Screen Size x , y
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()


while True: # this comand make the screen run forever
    for event in pygame.event.get(): #This method get all the events
        if event.type == pygame.QUIT: # If the user desice to leave the game
            pygame.quit()
            exit() # exit game

        # Draw all our elelemtns
        #Update everything
    pygame.display.update()
    clock.tick(60) # This is the frame of the velocity of the game please do not change it





























































































