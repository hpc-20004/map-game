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

#setup
pygame.init()
clock = pygame.time.Clock()

#create display surface
screen = pygame.display.set_mode((900,600))
screen_rect = screen.get_rect()

pygame.display.set_caption('name work in progress')

# Player class
class Player:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

#variables
move = 5
map_x = 540
map_y = -50

#player
thief = Player(450, 300, 50, 50, 5) #x and y values are in the center but this places the thief 'top left' in the middle
thief.rect.center = screen_rect.center #puts player in the middle of the screen
 
#floors
floor_1_surface = pygame.image.load('floor_1.png').convert()
floor_1_surface = pygame.transform.rotozoom(floor_1_surface, 0, 1.3)
floor_1_rect = floor_1_surface.get_rect(center = screen_rect.center) #initially puts center at the screen center

#functions
def player_movement_vert(y):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        y += move #directions are reversed to simulate the player moving in the map
    if keys[pygame.K_s]:
        y -= move   
        
    return y
 
def player_movement_horz(x):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x += move   
    if keys[pygame.K_d]:
        x -= move

    return x

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    map_y = player_movement_vert(map_y)
    map_x = player_movement_horz(map_x)
    
    floor_1_rect = floor_1_surface.get_rect(center=(map_x, map_y))
    
    screen.fill((0,0,0))
    screen.blit(floor_1_surface,floor_1_rect)
    pygame.draw.rect(screen,(255,255,255),thief.rect)
    

    pygame.display.update()
    clock.tick(60) #frame rate
