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

#create display surface 900 x 600

#temporary dimensions for wall creating is 2496 x 1664      1920x1280

screen = pygame.display.set_mode((1920,1280))
screen_rect = screen.get_rect()

pygame.display.set_caption('name work in progress')

# Player class
class Player:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

class Wall:
    def __init__(self,x,y, width, height):
        self.rect = pygame.Rect(x,y,width,height)
        

#variables
move = 5
map_x = 960
map_y = 600

# 540, -50

#player
thief = Player(450, 300, 50, 50, 5) #x and y values are in the center but this places the thief 'top left' in the middle
thief.rect.center = screen_rect.center #puts player in the middle of the screen
 
#floors
floor_1_surface = pygame.image.load('floor_1.png').convert()
floor_1_surface = pygame.transform.rotozoom(floor_1_surface, 0, 1)
floor_1_rect = floor_1_surface.get_rect(center = screen_rect.center) #initially puts center at the screen center

#walls
wall_list = []

#library
lib_top = wall_list.append(Wall(205,675,655-205,10))
lib_right_top = wall_list.append(Wall(650,675,10,850-675))
lib_right_bottom = wall_list.append(Wall(650,920,10,1030-920))

#dining
din_top = wall_list.append(Wall(210,195,560-205,10))
din_lib_left = wall_list.append(Wall(205,200,10,1030-200))
din_right_top = wall_list.append(Wall(555,195,10,530-195))
din_right_bottom = wall_list.append(Wall(555,600,10,675-600))

#cleaning room
cleaning_left = wall_list.append(Wall(780,135,10,485-135))

#kitchen
kit_cle_bottom = wall_list.append(Wall(710,485,1020-710,10))
kit_bottom_mid = wall_list.append(Wall(1090,485,1135-1090,10))
#kit_left_top = 

#stair walls
stair_1_left = wall_list.append(Wall(800,485,10,725-485))
stair_1_right = wall_list.append(Wall(960,485,10,725-485))

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

def draw_walls(list):
    for wall in list:
        pygame.draw.rect(screen,(255,255,255),wall.rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            
    map_y = player_movement_vert(map_y)
    map_x = player_movement_horz(map_x)
    
    floor_1_rect = floor_1_surface.get_rect(center=(map_x, map_y))
    
    screen.fill((0,0,0))
    screen.blit(floor_1_surface,floor_1_rect)
    pygame.draw.rect(screen,(255,255,255),thief.rect)
    draw_walls(wall_list)

    pygame.display.update()
    clock.tick(60) #frame rate
