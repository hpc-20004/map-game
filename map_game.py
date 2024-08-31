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

#separate animation clock
ANIMATION = pygame.USEREVENT
pygame.time.set_timer(ANIMATION, 200)#rate


#create display surface 900 x 600
screen = pygame.display.set_mode((900,600))
screen_rect = screen.get_rect()

pygame.display.set_caption('name work in progress')

#player class
class Player:
    def __init__(self,surface, x, y, width, height, speed,moving):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.rect.center = screen_rect.center
        self.moving = moving

    def move(self, x, y, walls):
        #move horizontally
        self.rect.x += x
        for wall in walls:
            if self.moving:
                if self.rect.colliderect(wall.rect):
                    if x > 0:  #hit the left side of wall
                        self.rect.right = wall.rect.left
                    if x < 0:  #hit the right side of wall
                        self.rect.left = wall.rect.right

        #move vertically
        self.rect.y += y
        for wall in walls:
            if self.moving:
                if self.rect.colliderect(wall.rect):
                    if y > 0:  #hit the top side of wall
                        self.rect.bottom = wall.rect.top
                    if y < 0:  #hit the bottom side of wall
                        self.rect.top = wall.rect.bottom

    def player_movement(self, walls, map_offset):
        keys = pygame.key.get_pressed()
        x, y = 0, 0
        
        if keys[pygame.K_w]:
            y = -self.speed #up
            self.moving = True
        if keys[pygame.K_s]:
            y = self.speed #down
            self.moving = True
        if keys[pygame.K_a]:
            x = -self.speed #left
            self.moving = True
        if keys[pygame.K_d]:
            x = self.speed #right
            self.moving = True

        #change player position and map offset based on player movement
        if self.rect.left + x < 0 or self.rect.right + x > screen_rect.width:
            map_offset[0] -= x
        else:
            self.move(x, 0, walls)

        if self.rect.top + y < 0 or self.rect.bottom + y > screen_rect.height:
            map_offset[1] -= y
        else:
            self.move(0, y, walls)

        return self.moving

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

#draw walls
def draw_walls(list, map_x, map_y):
    for wall in list:
        wall.update_position(map_x, map_y)
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)

#variables
speed = 5
map_x = 540
map_y = -50
collide = False
thief_frame = 0
moving = False

#player
thief_sprites = [pygame.image.load('thief/tile000.png').convert(),
                pygame.image.load('thief/tile001.png').convert(),
                pygame.image.load('thief/tile002.png').convert(),
                pygame.image.load('thief/tile003.png').convert(),
                pygame.image.load('thief/tile004.png').convert(),
                pygame.image.load('thief/tile005.png').convert(),
                pygame.image.load('thief/tile006.png').convert(),
                pygame.image.load('thief/tile007.png').convert(),
                pygame.image.load('thief/tile008.png').convert(),
                pygame.image.load('thief/tile009.png').convert(),
                pygame.image.load('thief/tile010.png').convert(),
                pygame.image.load('thief/tile011.png').convert()]

thief = Player(thief_sprites[8],450, 300, 50, 50, 5,moving) #x and y values are in the center but this places the thief 'top left' in the middle
# thief.rect.center = screen_rect.center

current_sprite = thief_sprites[8]

#set up tiles?
tile_size = 20

#floors
floor_1_surface = pygame.image.load('floor_1.png').convert()
floor_1_rect = floor_1_surface.get_rect(center = (540,-50)) #initially puts center at the screen center

#screen's center offset
center_offset_x = screen_rect.centerx -30
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

#starting map offset
map_offset = [0, 0] 

#game loop
while True:
    keys = pygame.key.get_pressed()
    moving = False  #reset moving status before checking keys

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())  #for checking coordinates

        if event.type == ANIMATION:
            if keys[pygame.K_w]:
                thief_frame = (thief_frame - 1) % 3 
            if keys[pygame.K_s]:
                thief_frame = (thief_frame + 1) % 3 + 6
            if keys[pygame.K_a]:
                thief_frame = (thief_frame + 1) % 3 + 9  
            if keys[pygame.K_d]:
                thief_frame = (thief_frame + 1) % 3 + 3  

    moving = thief.player_movement(wall_list, map_offset)

    #update the current sprite based on the animation frame
    current_sprite = thief_sprites[thief_frame]
    thief.surface = current_sprite

    #update floor position
    floor_1_rect = floor_1_surface.get_rect(center=(map_x + map_offset[0], map_y + map_offset[1]))

    #draw everything
    screen.fill((0, 0, 0))
    screen.blit(floor_1_surface, floor_1_rect)
    screen.blit(thief.surface, thief.rect)

    draw_walls(wall_list, map_offset[0], map_offset[1])

    pygame.display.update()
    clock.tick(60)  #frame rate

