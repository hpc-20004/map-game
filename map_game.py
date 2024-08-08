"""
----------------------------------------------------------------
Project: 3.7 + 3.8 Game Programming Assessment
Standard: AS91906, AS91907
School: Hauraki Plains College
Author: Erin Aralar
Date: August 2024
Python: 3.11
----------------------------------------------------------------
"""

#imports
import pygame, sys

from pygame.locals import QUIT

#Setup
pygame.init()
clock = pygame.time.Clock()

#Create display surface
screen = pygame.display.set_mode((900,600))

pygame.display.set_caption('name work in progress')

#variables
move = 10

#players
player1_rect = pygame.Rect(450,300,50,50)
 
#functions
def player_movement():
    keys = pygame.key.get_pressed()
    #player 1 movement
    if keys[pygame.K_a]:
        player1_rect.x -= move   
    if keys[pygame.K_d]:
        player1_rect.x += move
    if keys[pygame.K_w]:
        player1_rect.y -= move
    if keys[pygame.K_s]:
        player1_rect.y += move   
         


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    player_movement()
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),player1_rect)

    pygame.display.update()
    clock.tick(60) #frame rate
