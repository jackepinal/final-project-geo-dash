import pygame
import time
import random

pygame.init()

#Character inits
player_width = 55
player_height = 55

#Base colors, can be updated
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yella = (255, 255, 0)
see_thru_blue = (0, 0, 255, 128)

#Screen inits
screen_width = 1200
screen_height = 1000

screen_window = pygame.display.set_mode((screen_width, screen_height))

#Starting Screen
pygame.font.get_fonts()

def geo_intro():
   
    geo_intro = True
    
    while True:
        #in event of quit
        for event in pygame.event.get():
            if event == quit:
                pygame.quit
                quit()
        screen_window.fill(see_thru_blue)
        