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
map_x = -450
map_y = -300

#player
player_rect = pygame.Rect(450,300,50,50)
 
#floors
floor_1_surface = pygame.image.load('floor_1.png').convert()
floor_1_rect = floor_1_surface.get_rect(center = (map_x,map_y))

#functions
def player_movement_vert(y):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        y -= move
    if keys[pygame.K_s]:
        y += move   
 
def player_movement_horz(x):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x -= move   
    if keys[pygame.K_d]:
        x += move

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    map_y = player_movement_vert(map_y)
    map_x = player_movement_horz(map_x)
    
    screen.fill((0,0,0))
    screen.blit(floor_1_surface,floor_1_rect)
    pygame.draw.rect(screen,(255,255,255),player_rect)
    

    pygame.display.update()
    clock.tick(60) #frame rate
