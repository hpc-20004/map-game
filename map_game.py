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

screen = pygame.display.set_mode((900,600))
screen_rect = screen.get_rect()

pygame.display.set_caption('name work in progress')

#Player class
class Player:
    def __init__(self, x, y, width, height, speed,moving):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.x = x
        self.y = y
        self.moving = moving
        
    def player_movement_vert(self, collide):
        keys = pygame.key.get_pressed()
        self.moving = False
        
        if self.y < 150:
            self.y = 150
        if self.y > 450:
            self.y = 450
        
        if collide == False:
            if keys[pygame.K_w]:
                self.y -= speed #directions are reversed to simulate the player moving in the map
                self.moving = True
            if keys[pygame.K_s]:
                self.y += speed 
                self.moving = True
        
        return self.y
 
    def player_movement_horz(self, collide):
        keys = pygame.key.get_pressed()
        self.moving = False
        
        if self.x < 225:
            self.x = 225
        if self.x > 675:
            self.x = 675
             
        if collide == False:
            if keys[pygame.K_a]:
                self.x -= speed   
                self.moving = True
            if keys[pygame.K_d]:
                self.x += speed
                self.moving = True

        return self.x
    
    # def wall_collision(self,list,collide):
    #     for wall in list:
    #         collide = pygame.Rect.colliderect(self.rect, wall.rect)
    #         if collide:
    #             print('collide')    
    #         return collide
            

#wall class
class Wall:
    def __init__(self,x,y, width, height):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        
    # def move_wall(self, map_x, map_y, moving):
    #     if moving == True:
    #         self.rect.x = map_x
    #         self.rect.y = map_y
        

#variables
speed = 5
map_x = 540
map_y = -50
collide = False

# 540, -50

#player
thief = Player(450, 300, 50, 50, 5,False) #x and y values are in the center but this places the thief 'top left' in the middle
thief.rect.center = screen_rect.center #puts player in the middle of the screen
 
#floors
floor_1_surface = pygame.image.load('floor_1.png').convert()
# floor_1_surface = pygame.transform.rotozoom(floor_1_surface, 0, 1)
floor_1_rect = floor_1_surface.get_rect(center = (540,-50)) #initially puts center at the screen center

#screen's center offset
center_offset_x = screen_rect.centerx - 30
center_offset_y = screen_rect.centery +355

#walls (relative to the center of the screen)
wall_list = []

#library
lib_top = wall_list.append(Wall(205 - center_offset_x, 675 - center_offset_y, 655-205, 10))
lib_right_top = wall_list.append(Wall(650 - center_offset_x, 675 - center_offset_y, 10, 850-675))
lib_right_bottom = wall_list.append(Wall(650 - center_offset_x, 920 - center_offset_y, 10, 1030-920))
lib_bottom = wall_list.append(Wall(205 - center_offset_x, 1030 - center_offset_y, 685-205, 10))

#dining
din_top = wall_list.append(Wall(210 - center_offset_x, 195 - center_offset_y, 560-205, 10))
din_lib_left = wall_list.append(Wall(205 - center_offset_x, 200 - center_offset_y, 10, 1030-200))
din_right_top = wall_list.append(Wall(555 - center_offset_x, 195 - center_offset_y, 10, 530-195))
din_right_bottom = wall_list.append(Wall(555 - center_offset_x, 600 - center_offset_y, 10, 675-600))

#cleaning room
cleaning_right = wall_list.append(Wall(780 - center_offset_x, 135 - center_offset_y, 10, 485-135))
cleaning_top = wall_list.append(Wall(555 - center_offset_x, 260 - center_offset_y, 785-560, 10))
cleaning_bottom_left = wall_list.append(Wall(560 - center_offset_x, 485 - center_offset_y, 640-560, 10))

#kitchen
kit_cle_bottom = wall_list.append(Wall(710 - center_offset_x, 485 - center_offset_y, 1020-710, 10))
kit_bottom_mid = wall_list.append(Wall(1090 - center_offset_x, 485 - center_offset_y, 1135-1090, 10))
kit_right_top = wall_list.append(Wall(1100 - center_offset_x, 135 - center_offset_y, 10, 265-135))
kit_liv_top = wall_list.append(Wall(1100 - center_offset_x, 260 - center_offset_y, 1645-1100, 10))
kit_bottom_right = wall_list.append(Wall(1135 - center_offset_x, 710 - center_offset_y, 1365-1135, 10))
kit_left_top = wall_list.append(Wall(1130 - center_offset_x, 485 - center_offset_y, 10, 565-485))
kit_left_bottom = wall_list.append(Wall(1130 - center_offset_x, 630 - center_offset_y, 10, 810-630))

#living area
living_left_top = wall_list.append(Wall(1355 - center_offset_x, 265 - center_offset_y, 10, 715-265))
living_left_bottom = wall_list.append(Wall(1130 - center_offset_x, 965 - center_offset_y, 10, 1030-965))
living_right = wall_list.append(Wall(1645 - center_offset_x, 265 - center_offset_y, 10, 1030-265))
living_bottom = wall_list.append(Wall(1105 - center_offset_x, 1030 - center_offset_y, 1645-1105, 10))

#foyer
foyer_left = wall_list.append(Wall(685 - center_offset_x, 1030 - center_offset_y, 10, 1160-1030))
foyer_right = wall_list.append(Wall(1105 - center_offset_x, 1030 - center_offset_y, 10, 1160-1030))
foyer_bottom_left = wall_list.append(Wall(685 - center_offset_x, 1160 - center_offset_y, 860-685, 10))
foyer_bottom_right = wall_list.append(Wall(925 - center_offset_x, 1160 - center_offset_y, 1105-925, 10))

#stair walls
stair_1_left = wall_list.append(Wall(800 - center_offset_x, 485 - center_offset_y, 10, 725-485))
stair_1_right = wall_list.append(Wall(960 - center_offset_x, 485 - center_offset_y, 10, 725-485))


#functions

def draw_walls(list):
    for wall in list:
        #wall.move_wall(map_x, map_y,thief.moving)
        pygame.draw.rect(screen,(255,255,255),wall.rect)

# def movement(list,speed):
#     for wall in list:
#         keys = pygame.key.get_pressed()
           
#         if keys[pygame.K_a]:
#             wall.rect.x += speed
            
#         if keys[pygame.K_d]:
#             wall.rect.x -= speed
            
#         if keys[pygame.K_w]:
#             wall.rect.y += speed 
            
#         if keys[pygame.K_s]:
#             wall.rect.y -= speed
        

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            
    # collide = Player.wall_collision(thief,wall_list,collide)      

    thief.rect.centery = Player.player_movement_vert(thief, collide)
    thief.rect.centerx = Player.player_movement_horz(thief, collide)
   
    # collide = Player.wall_collision(thief,wall_list,collide)  
    #collide = False
    # movement(wall_list,speed)
    
    for wall in wall_list:
        collide = pygame.Rect.colliderect(thief.rect, wall.rect)
        if collide:
            print('collide')   
   
            speed = 0
        else:
            speed = 5
    
    floor_1_rect = floor_1_surface.get_rect(center=(map_x,map_y))
    
    screen.fill((0,0,0))
    screen.blit(floor_1_surface,floor_1_rect)
    pygame.draw.rect(screen,(255,255,255),thief.rect)
    
    draw_walls(wall_list) 

    pygame.display.update()
    clock.tick(60) #frame rate
