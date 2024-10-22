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
from walls import create_walls

#setup
pygame.init()
clock = pygame.time.Clock()

#separate animation clock
ANIMATION = pygame.USEREVENT
pygame.time.set_timer(ANIMATION, 200)#  rate


#create display surface 900 x 600
SCREEN = pygame.display.set_mode((900,600))
screen_rect = SCREEN.get_rect()

pygame.display.set_caption("Thief's Gambit")

#player class
class Player:
    def __init__(self, surface, x, y, width, height, speed, moving):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.rect.center = screen_rect.center
        self.moving = moving
        self.x = x 
        self.y = y

    def player_movement(self, walls, map_offset):
        keys = pygame.key.get_pressed()
        x, y = 0, 0
        
        if keys[pygame.K_w]:
            y = self.speed  #   move map down
            self.moving = True
        if keys[pygame.K_s]:
            y = -self.speed  #  move map up
            self.moving = True
        if keys[pygame.K_a]:
            x = self.speed  #   move map right
            self.moving = True
        if keys[pygame.K_d]:
            x = -self.speed  #  move map left
            self.moving = True
            
        

        #check for collisions and update the map offset
        for wall in walls:
            #update wall positions based on the current offset
            wall.update_position(map_offset[0] + x, map_offset[1] + y)

            if self.rect.colliderect(wall.rect):  #detect collisioms
                if x > 0:  #    moving right, push map back to the left
                    x = 0
                if x < 0:  #    moving left, push map back to the right
                    x = 0
                if y > 0:  #    moving down, push map back up
                    y = 0
                if y < 0:  #    moving up, push map back down
                    y = 0

        #change the offset based on how the map has moved
        map_offset[0] += x
        map_offset[1] += y
        
        return self.moving
    
#game item class
class Item:
    def __init__(self, name, min_x_offset, max_x_offset, min_y_offset, max_y_offset, floor, found):
        self.name = name
        self.min_x_offset = min_x_offset
        self.max_x_offset = max_x_offset
        self.min_y_offset = min_y_offset
        self.max_y_offset = max_y_offset
        self.floor = floor # once floors are implemented in the find items method check if player's floor and item floor are the same
        self.found = found
        
    def find_items(self, map_offset_x, map_offset_y):
        keys = pygame.key.get_pressed() # to see if c gets pressed
        
        if self.min_x_offset <= map_offset_x <= self.max_x_offset and self.min_y_offset <= map_offset_y <= self.max_y_offset:
            if keys[pygame.K_c]:
                print("{} found".format(self.name))
                self.found = True
                
#room class
class Room:
    def __init__(self, name, min_x_offset, max_x_offset, min_y_offset, max_y_offset, floor, locked, in_room):
        self.name = name
        self.min_x_offset = min_x_offset
        self.max_x_offset = max_x_offset
        self.min_y_offset = min_y_offset
        self.max_y_offset = max_y_offset
        self.floor = floor # once floors are implemented in the find items method check if player's floor and room floor are the same
        self.locked = locked
        self.in_room = in_room
        
    def check_room_location(self, map_offset_x, map_offset_y, previous_player_location, current_floor):
        if self.min_x_offset <= map_offset_x <= self.max_x_offset and self.min_y_offset <= map_offset_y <= self.max_y_offset:
            if self.floor == current_floor:
                self.in_room = True
                return self.name
            # else:
            #     self.in_room = False
            #     return previous_player_location
                
        else:
            self.in_room = False
            return previous_player_location # if they're still in the same room?

#wall class
class Wall:
    def __init__(self, x, y, width, height):
        self.original_x = x
        self.original_y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def update_position(self, map_x, map_y):
        #update wall's position based on map's position
        self.rect.x = self.original_x + map_x
        self.rect.y = self.original_y + map_y
        
            
    def draw(self, surface, map_x, map_y, current_floor,list):
        #update position before drawing
        self.update_position(map_x, map_y)
        
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

#draw walls
def draw_walls(current_wall_list, surface, map_x, map_y, current_floor):
    for wall in current_wall_list:
        wall.draw(surface, map_x, map_y, current_floor, current_wall_list)

#variables
speed = 5
MAP_X = 540
MAP_Y = -50
collide = False
thief_frame = 0
moving = False
player_location = 0
current_floor = 1 # player starts at ground level

#item list
item_list = []

book_item = Item("The Great Gutsby", 525,580,195,205,1,False)
item_list.append(book_item)

master_key_item = Item("Master Bedroom Key",265,285,545,600,1,False)
item_list.append(master_key_item)

tv_item = Item("TV",-690,-580,590,595,1,False)
item_list.append(tv_item)

#room list
room_list = []

# floor 1
foyer = Room("Foyer",-240,285,-180,410,1,False,False)
room_list.append(foyer)

library = Room("Library",240,635,-50,205,1,False,False)
room_list.append(library)

dining = Room("Dining Room",335,635,305,655,1,False,False)
room_list.append(dining)

cleaning = Room("Cleaning Supplies Closet",110,285,495,610,1,False,False)
room_list.append(cleaning)

#   L shaped rooms are  
kitchen_left = Room("Kitchen",-265,60,495,720,1,False,False)
kitchen_right = Room("Kitchen",-465,-266,270,595,1,False,False)
room_list.append(kitchen_left)
room_list.append(kitchen_right)

living_left = Room("Living Room",-514,-290,-50,185,1,False,False)
living_right = Room("Living Room",-755,-515,-50,595,1,False,False)
room_list.append(living_left)
room_list.append(living_right)


# FLoor 2
ensuite = Room("Ensuite",510,640,300,375,2,True,False)
room_list.append(ensuite)

#player
THIEF_SPRITES = []
for sprite in range(12):  #tile000.png to tile011.png
    
    #image name
    sprite_file = f'thief/tile{sprite:03}.png'  #:03 so it has 3 digits
        
    #load
    original_sprite = pygame.image.load(sprite_file).convert()
        
    #get sprite dimensions
    original_width, original_height = original_sprite.get_size()
        
    #change ONLY height to 55px
    new_height = 50
    new_width = (50/original_height) * original_width
    new_size = (new_width, new_height)
        
    resized_sprite = pygame.transform.scale(original_sprite, new_size)
        
    #append to sprite list
    THIEF_SPRITES.append(resized_sprite)

thief = Player(THIEF_SPRITES[8],450, 300, 50, 50, 5,moving) #x and y values are in the center but this places the thief 'top left' in the middle
# thief.rect.center = screen_rect.center

current_sprite = THIEF_SPRITES[8]

#set up tiles?
TILE_SIZE = 20

#floors
floor_1_surface = pygame.image.load('floor 1.png').convert()
floor_2_surface = pygame.image.load('floor 2.png').convert()
floor_3_surface = pygame.image.load('floor 3.png').convert()

floor_shown_surface = floor_1_surface #  starts at floor 1 
floor_rect = floor_shown_surface.get_rect(center = (540,-50)) # initially puts center at the entrance

#screen's center offset
CENTER_OFFSET_X = screen_rect.centerx -30
CENTER_OFFSET_Y = screen_rect.centery +355

#walls (relative to the center of the screen)
current_wall_list, stair_1_top, stair_2_down = create_walls(Wall, CENTER_OFFSET_X, CENTER_OFFSET_Y, current_floor)

#starting map offset
map_offset = [0, 0]  #x offset, y offset

#game loop
while True:
    keys = pygame.key.get_pressed()
    moving = False  # reset moving status before checking keys

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())  # for checking coordinates
            print(map_offset[0])
            print(map_offset[1])
            print(player_location)
            print("current floor {}".format(current_floor))

        if event.type == ANIMATION: #   animation
            if keys[pygame.K_w]:
                thief_frame = (thief_frame - 1) % 3 
            if keys[pygame.K_s]:
                thief_frame = (thief_frame + 1) % 3 + 6
            if keys[pygame.K_a]:
                thief_frame = (thief_frame + 1) % 3 + 9  
            if keys[pygame.K_d]:
                thief_frame = (thief_frame + 1) % 3 + 3  
        if event.type == pygame.KEYDOWN: #testing floors
            if event.key == pygame.K_SPACE:
                if floor_shown_surface == floor_1_surface:
                    floor_shown_surface = floor_2_surface  
                else:
                    floor_shown_surface = floor_1_surface 

    moving = thief.player_movement(current_wall_list, map_offset)
    
    #check if any items are found
    for item in item_list:
        item.find_items(map_offset[0],map_offset[1])
        
    #check what room the player's in
    for room in room_list:
        player_location = room.check_room_location(map_offset[0],map_offset[1],player_location, current_floor)
        
    #check what floor the player's in
    if floor_shown_surface == floor_1_surface:
        current_floor = 1
    elif floor_shown_surface == floor_2_surface:
        current_floor = 2
    elif floor_shown_surface == floor_3_surface:
        current_floor = 3

    # update the current sprite based on the animation frame
    current_sprite = THIEF_SPRITES[thief_frame]
    thief.surface = current_sprite

    # update floor position and floor
    floor_rect = floor_shown_surface.get_rect(center=(MAP_X + map_offset[0], MAP_Y + map_offset[1]))
    
    if thief.rect.colliderect(stair_1_top.rect):
        floor_shown_surface = floor_2_surface

    # draw everything
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(floor_shown_surface, floor_rect)
    SCREEN.blit(thief.surface, thief.rect)

    current_wall_list, stair_1_top, stair_2_down = create_walls(Wall, CENTER_OFFSET_X, CENTER_OFFSET_Y, current_floor)
    draw_walls(current_wall_list, SCREEN, map_offset[0], map_offset[1], current_floor) #get rid of this to make the walls invisible eventually

    pygame.display.update()
    clock.tick(60)  # frame rate
    


