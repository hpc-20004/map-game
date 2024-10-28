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

#   imports
import pygame, sys
from pygame.locals import QUIT
from walls import create_walls
from rooms import create_rooms
from doors import create_doors

#   setup
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

#   separate animation clock
ANIMATION = pygame.USEREVENT
pygame.time.set_timer(ANIMATION, 200)#  rate

#   time limit
time_left = 5 * 60#   5 minutes

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

minutes = time_left // 60
seconds = time_left % 60

#   create display surface 900 x 600
SCREEN = pygame.display.set_mode((900,600))
SCREEN_RECT = SCREEN.get_rect()

SCREEN_CENTER_X = 450
SCREEN_CENTER_Y = 300

#   screen's center offset
CENTER_OFFSET_X = SCREEN_RECT.centerx -30
CENTER_OFFSET_Y = SCREEN_RECT.centery +355

#   starting map offset
map_offset = [0, 0]  #  x offset, y offset

pygame.display.set_caption("Thief's Gambit") #  game name

#   player class
class Player:
    def __init__(self, surface, x, y, speed, moving):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.speed = speed
        self.rect.center = SCREEN_RECT.center
        self.moving = moving
        self.x = x 
        self.y = y

    def player_movement(self, walls, doors, map_offset, FONT, items_collected, no_of_items, game_endings):
        keys = pygame.key.get_pressed()
        x, y = 0, 0
        door_dialogue_surface, door_dialogue_rect = None, None
        
        if keys[pygame.K_w]:
            y = self.speed  #   move map down
            self.moving = True
        elif keys[pygame.K_s]:
            y = -self.speed  #  move map up
            self.moving = True
        if keys[pygame.K_a]:
            x = self.speed  #   move map right
            self.moving = True
        elif keys[pygame.K_d]:
            x = -self.speed  #  move map left
            self.moving = True
            

        #   check for collisions and update the map offset
        for wall in walls:
            #   update wall positions based on the current offset
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

        #   check for collisions with doors
        for door in doors:
            door.draw_doors(SCREEN, map_offset[0], map_offset[1])
            
            x_distance_from_door = self.x - door.rect.x
            y_distance_from_door = self.y - door.rect.y
            x_door_hit = door.w * 2
            y_door_hit = door.l + 30
        
            if door.locked:

                if x_distance_from_door > 0: # doors on the left of player
                    if x_distance_from_door < x_door_hit:
                        if y_distance_from_door < y_door_hit and y_distance_from_door > - y_door_hit:
                            if door.orientation == 'horizontal':
                                x = -1  # sort of 'knockback' the player so they don't get stuck and it's also visual feedback that they can't go in
                            
                                # create door locked dialogue
                                door_dialogue_surface, door_dialogue_rect = door.locked_dialogue(FONT,SCREEN_CENTER_X,SCREEN_CENTER_Y)
                    
                if x_distance_from_door < 0: # doors on the right of player
                    if x_distance_from_door > - x_door_hit:
                        if y_distance_from_door < y_door_hit and y_distance_from_door > - y_door_hit:
                            if door.orientation == 'horizontal':
                                x = 1
                                # create door locked dialogue
                                door_dialogue_surface, door_dialogue_rect = door.locked_dialogue(FONT,SCREEN_CENTER_X,SCREEN_CENTER_Y)
                            
                if y_distance_from_door > 0: # door above player
                    if y_distance_from_door < y_door_hit:
                        if door.orientation == 'vertical':
                            if 0 < x_distance_from_door < door.w: #   only stops the player from going up when they're aligned with the door
                                y = -1
                                # create door locked dialogue
                                door_dialogue_surface, door_dialogue_rect = door.locked_dialogue(FONT,SCREEN_CENTER_X,SCREEN_CENTER_Y)
                    
                if y_distance_from_door < 0: # door below player
                    if y_distance_from_door > - y_door_hit:
                        if door.orientation == 'vertical':
                            if 0 < x_distance_from_door < door.w:
                                y = 1
                                # create door locked dialogue
                                door_dialogue_surface, door_dialogue_rect = door.locked_dialogue(FONT,SCREEN_CENTER_X,SCREEN_CENTER_Y)
                                
            if door.hidden_exit and not door.locked:
                
                if self.rect.colliderect(door.rect):
                    
                    if items_collected < no_of_items: #   fire exit unlocked before collecting all items
                        
                        hidden_exit_dialogue_surface, hidden_exit_dialogue_rect = door.hidden_exit_dialogue(FONT, "There's still more to steal!", SCREEN_CENTER_X)
                        
                    else:
                        
                        hidden_exit_dialogue_surface, hidden_exit_dialogue_rect = door.hidden_exit_dialogue(FONT, None, SCREEN_CENTER_X)
                        
                        game_over = True
                        
                        if door.room == "Powder Room Window":
                            ending = game_endings[0]
                        elif door.room == "Front Door":
                            ending = game_endings[1]
                        elif door.room == "Fire Exit":
                            ending = game_endings[2]
                           
                        
                else:
                    hidden_exit_dialogue_surface, hidden_exit_dialogue_rect = door.hidden_exit_dialogue(FONT, None, SCREEN_CENTER_X)
                    ending = None
                    game_over = None
            else:
                    hidden_exit_dialogue_surface, hidden_exit_dialogue_rect = door.hidden_exit_dialogue(FONT, None, SCREEN_CENTER_X)
                    ending = None
                    game_over = None

        #   change the offset based on how the map has moved
        map_offset[0] += x
        map_offset[1] += y

        return self.moving, door_dialogue_surface, door_dialogue_rect, hidden_exit_dialogue_surface, hidden_exit_dialogue_rect, ending, game_over
    
#   game item class
class Item:
    def __init__(self, name, image, x, y, l, w, min_x_offset, max_x_offset, min_y_offset, max_y_offset, floor, found):
        
        self.name = name
        self.image = image
        if image: #   only make these for items that have an image
            
            self.surface = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(l,w))
        
        self.x = x
        self.y = y
        self.l = l
        self.w = w
            
        self.min_x_offset = min_x_offset
        self.max_x_offset = max_x_offset
        self.min_y_offset = min_y_offset
        self.max_y_offset = max_y_offset
        self.floor = floor # once floors are implemented in the find items method check if player's floor and item floor are the same
        self.found = found
        
    def find_items(self, map_offset_x, map_offset_y,current_floor,items_collected):
        keys = pygame.key.get_pressed() # to see if c gets pressed
        
        if not self.found:
            
            if self.floor == current_floor:
                
                if self.min_x_offset <= map_offset_x <= self.max_x_offset and self.min_y_offset <= map_offset_y <= self.max_y_offset:
                    if keys[pygame.K_c]:
                        
                        self.found = True
                       
                        items_collected += 1
                        
                        channel2.play(cha_ching)
                        
                        return items_collected
                    
                    else:
            
                        items_collected = items_collected # number of items collected stays the same so the same value is returned
            
                        return items_collected
                else:
            
                        items_collected = items_collected # number of items collected stays the same so the same value is returned
            
                        return items_collected
            else:
            
                        items_collected = items_collected # number of items collected stays the same so the same value is returned
            
                        return items_collected
        else:
            
                        items_collected = items_collected # number of items collected stays the same so the same value is returned
            
                        return items_collected
        
    def draw_items(self,mox,moy,current_floor):

        if self.found == False and self.image  and self.floor == current_floor:
            
            self.rect = self.surface.get_rect(center = (self.x+mox, self.y+moy))
            
            SCREEN.blit(self.surface,self.rect)
                
#   room class
class Room:
    def __init__(self, name, min_x_offset, max_x_offset, min_y_offset, max_y_offset, floor, locked, in_room, map_coords):
        self.name = name
        self.min_x_offset = min_x_offset
        self.max_x_offset = max_x_offset
        self.min_y_offset = min_y_offset
        self.max_y_offset = max_y_offset
        self.floor = floor # once floors are implemented in the find items method check if player's floor and room floor are the same
        self.locked = locked
        self.in_room = in_room
        self.map_coords = map_coords
        
    def check_room_location(self, map_offset_x, map_offset_y, previous_player_location, current_floor):
        if self.floor == current_floor:
            if self.min_x_offset <= map_offset_x <= self.max_x_offset and self.min_y_offset <= map_offset_y <= self.max_y_offset:
                self.in_room = True
                return self.name
            else:
                self.in_room = False
                return previous_player_location
                
        else:
            self.in_room = False
            return previous_player_location # if they're still in the same room?

class Door: #   doors 70px tall
    def __init__(self,room, image,x,y,l,w,locked, hidden_exit,orientation):
        self.room = room
        self.image = image
        if image:
            self.surface = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (w,l))
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.locked = locked
        self.hidden_exit = hidden_exit
        self.orientation = orientation
        self.rect = pygame.Rect(self.x,self.y,self.w,self.l)
        
    def locked_dialogue(self,FONT, SCREEN_CENTER_X, SCREEN_CENTER_Y):
        door_locked_dialogue_surface = FONT.render(f'{self.room} is locked.', True, (255,255,255)) 
        door_locked_dialogue_rect = door_locked_dialogue_surface.get_rect(center = (SCREEN_CENTER_X,500))
        
        return door_locked_dialogue_surface, door_locked_dialogue_rect
    
    def hidden_exit_dialogue(self,FONT, message, SCREEN_CENTER_X):
        hidden_exit_dialogue_surface = FONT.render(message , True, (255,255,255))
        hidden_exit_dialogue_rect = hidden_exit_dialogue_surface.get_rect(center = (SCREEN_CENTER_X,500))
        
        return hidden_exit_dialogue_surface, hidden_exit_dialogue_rect

    def door_unlock(self):
        self.locked = False
        
    def unlock_hidden_exit(self, items_collected, no_of_items):
        #   unlock hidden exits once all items are collected
        if self.hidden_exit and items_collected == no_of_items: # if all items are collected  
            self.locked = False
        
    def draw_doors(self,SCREEN,mox,moy):
        if self.image:
            
            self.rect = self.surface.get_rect(center  = (self.x + (self.w/2) + mox, self.y + (self.l/2) + moy)) #   centre of each door
            SCREEN.blit(self.surface, self.rect)
        else:
            self.rect = pygame.Rect(self.x + mox,self.y + moy,self.w,self.l)
            
#   wall class
class Wall:
    def __init__(self, x, y, width, height):
        self.original_x = x
        self.original_y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def update_position(self, map_x, map_y):
        #   update wall's position based on map's position
        self.rect.x = self.original_x + map_x
        self.rect.y = self.original_y + map_y
        
            
    def draw(self, surface, map_x, map_y, current_floor,list):
        #   update position before drawing
        self.update_position(map_x, map_y)
        
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

#   functions
#   draw walls
def draw_walls(current_wall_list, surface, map_x, map_y, current_floor):
    for wall in current_wall_list:
        wall.draw(surface, map_x, map_y, current_floor, current_wall_list)
     
#   draw dialogue
def draw_dialogue(door_dialogue_showing, SCREEN, door_dialogue_surface, door_dialogue_rect):
    if door_dialogue_showing:
        SCREEN.blit(door_dialogue_surface,door_dialogue_rect)
    
#   reset game
def reset_game(game_over, floor_shown_surface, items_collected, ending, item_list, current_door_list, map_offset, time_left, end_sound_played):
    game_over = False
    floor_shown_surface = floor_1_surface
    items_collected = 0
    map_offset = [0,0]
    ending = None
    time_left = 5 * 60
    end_sound_played = False
    
    #   re lock doors
    for door in current_door_list:
        if door.hidden_exit or door.room == "Master Bedroom": 
            door.locked = True
            
    #   reset items
    for item in item_list:
        item.found = False
    
    return game_over, floor_shown_surface, items_collected, ending, item_list, current_door_list, map_offset, time_left, end_sound_played

#   variables and constants
#   game states
game_active = False
game_over = False
game_endings = ["Win: Jumped out the window!",
                "Win: Front door - why not?",
                "Win: Fire exit.. Where's the fire?",
                "Game over: The owners are back!"]

#   setup
speed = 3
MAP_X = 540
MAP_Y = -50
collide = False
thief_frame = 0
moving = False
player_location = 0
current_floor = 1 # player starts at ground level
items_collected = 0
ending = None
no_of_items = 7
end_sound_played = False

#   UI
ui_bg_showing = False
ui_shown = 0 #  should be either map or checklist

CHECKLIST_RED = (153,0,0)

instructions_showing = False

#   text
FONT = pygame.font.Font('assets/fonts/Pixel Lofi.otf',40)
LARGE_FONT = pygame.font.Font('assets/fonts/Pixel Lofi.otf',60)

door_dialogue_showing = False
item_dialogue_showing = False

time_left_surface = FONT.render(f"{minutes}:{seconds:02}", True, (255, 255, 255))
time_left_rect = time_left_surface.get_rect(center = (100,70))

#   audio
#   channels
#   music channel
channel1 = pygame.mixer.Channel(0)
channel1.set_volume(0.4) #  so the music's not too loud

#   sound effects channel
channel2 = pygame.mixer.Channel(1)
channel2.set_volume(0.5) #  so the sound effects don't hurt the users' ears

music = pygame.mixer.Sound('assets/audio/sneaky music.mp3')

cha_ching = pygame.mixer.Sound('assets/audio/cha-ching-sound.mp3')

yay = pygame.mixer.Sound('assets/audio/yay.mp3')

siren = pygame.mixer.Sound('assets/audio/siren.mp3')

#   player
THIEF_SPRITES = []
for sprite in range(12):  #tile000.png to tile011.png
    
    #   image name
    sprite_file = f'assets/images/thief/tile{sprite:03}.png'  #:03 so it has 3 digits
        
    #   load
    original_sprite = pygame.image.load(sprite_file).convert()
        
    #   get sprite dimensions
    original_width, original_height = original_sprite.get_size()
        
    #   change ONLY height to 55px
    new_height = 50
    new_width = (50/original_height) * original_width
    new_size = (new_width, new_height)
        
    resized_sprite = pygame.transform.scale(original_sprite, new_size)
        
    #   append to sprite list
    THIEF_SPRITES.append(resized_sprite)

thief = Player(THIEF_SPRITES[8], SCREEN_CENTER_X, SCREEN_CENTER_Y, 5,moving) #x and y values are in the center but this places the thief 'top left' in the middle
# thief.rect.center = screen_rect.center

current_sprite = THIEF_SPRITES[8]

#   item list
item_list = []

master_key_item = Item("Master Bedroom Key", "assets/images/items/key.png", 585 - CENTER_OFFSET_X, 390 - CENTER_OFFSET_Y, 40, 40, 265,285,545,600,1,False)
item_list.append(master_key_item)

book_item = Item("The Great Gutsby", None, 0,0,0,0, 525,580,195,205,1,False)
item_list.append(book_item)

tv_item = Item("TV", "assets/images/items/tv.png", 1505 - CENTER_OFFSET_X, 330 - CENTER_OFFSET_Y, 141, 141, -690, -580, 590, 595, 1, False)
item_list.append(tv_item)

violin_item = Item("Paganini's Violin","assets/images/items/violin.png",1125 - CENTER_OFFSET_X, 305 - CENTER_OFFSET_Y,30,30,-275,-215,640,685,3,False)
item_list.append(violin_item)

fire_exit_key_item = Item("Fire Exit Key","assets/images/items/key.png", 290 - CENTER_OFFSET_X, 650 - CENTER_OFFSET_Y, 40,40,525,635,260,330,2,False)
item_list.append(fire_exit_key_item)

painting_item = Item("'A Cloudy Night' Painting", "assets/images/items/painting.png",1095 - CENTER_OFFSET_X, 630 - CENTER_OFFSET_Y,80,50,-260,-205,295,310,3,False)
item_list.append(painting_item)

gold_item = Item("Bars of Gold","assets/images/items/gold.png", 655 - CENTER_OFFSET_X, 305 - CENTER_OFFSET_Y,50,50,185,255,635,695,3,False)
item_list.append(gold_item)

#   rooms
room_list = create_rooms(Room)

#   doors
current_door_list = create_doors(Door, CENTER_OFFSET_X, CENTER_OFFSET_Y,current_floor)

#   floors
floor_1_surface = pygame.image.load('assets/images/floors/floor 1.png').convert()
floor_2_surface = pygame.image.load('assets/images/floors/floor 2.png').convert()
floor_3_surface = pygame.image.load('assets/images/floors/floor 3.png').convert()

floor_shown_surface = floor_1_surface #  starts at floor 1 
floor_rect = floor_shown_surface.get_rect(center = (540,-50)) # initially puts center at the entrance

#   walls (relative to the center of the screen)
current_wall_list, stair_1_top, stair_2_down, left_2_up, right_2_up, left_3_down, right_3_down = create_walls(Wall, CENTER_OFFSET_X, CENTER_OFFSET_Y, current_floor)

# UI
# icons
UI_icon_size = 100

map_button_surface = pygame.transform.scale(pygame.image.load("assets/images/UI/map icon.png").convert_alpha(),(UI_icon_size,UI_icon_size))
map_button_rect = map_button_surface.get_rect(center = (800, 70))

checklist_button_surface = pygame.transform.scale(pygame.image.load("assets/images/UI/checklist icon.png").convert_alpha(),(UI_icon_size,UI_icon_size))
checklist_button_rect = checklist_button_surface.get_rect(center = (800,180))

ui_bg_surface = pygame.image.load("assets/images/UI/UI BG.png").convert_alpha()
ui_bg_rect = ui_bg_surface.get_rect(center = (SCREEN_CENTER_X, SCREEN_CENTER_Y))

ui_x_surface = pygame.transform.scale(pygame.image.load("assets/images/UI/temp x.png").convert_alpha(),(100,100)) # temporary until i get an x
ui_x_rect = ui_x_surface.get_rect(center = (780, 90))

# map
map_list = []

map_floor_1_surface = pygame.transform.scale(pygame.image.load("assets/images/UI/map floor 1.png").convert_alpha(),(600,400))

map_floor_2_surface = pygame.transform.scale(pygame.image.load("assets/images/UI/map floor 2.png").convert_alpha(),(600,400))

map_floor_3_surface = pygame.transform.scale(pygame.image.load("assets/images/UI/map floor 3.png").convert_alpha(),(600,400))

#  add them to the map list
map_list.append(map_floor_1_surface)

map_list.append(map_floor_2_surface)

map_list.append(map_floor_3_surface)

map_thief_icon_surface = pygame.image.load("assets/images/thief/tile007.png").convert_alpha()

map_thief_coordinates = []

# checklist
checklist_surface = pygame.image.load("assets/images/UI/checklist.png").convert_alpha()
checklist_rect = checklist_surface.get_rect(center = (SCREEN_CENTER_X,SCREEN_CENTER_Y))
checklist_thickness = 5 # might change this later

checklist_list = [
    pygame.Rect(76,180,350,checklist_thickness),
    pygame.Rect(80,240,560,checklist_thickness),
    pygame.Rect(77,290,50,checklist_thickness),
    pygame.Rect(79,350,270,checklist_thickness),
    pygame.Rect(75,410,229,checklist_thickness),
    pygame.Rect(77,470,260,checklist_thickness),
    pygame.Rect(76,530,230,checklist_thickness)
    ]

#   start screen
start_screen_surface = pygame.image.load("assets/images/UI/start screen.png").convert_alpha()
start_screen_rect = start_screen_surface.get_rect(center = (SCREEN_CENTER_X, SCREEN_CENTER_Y))

start_bg_screen_surface = pygame.image.load("assets/images/UI/start bg.png").convert()
start_bg_screen_rect = start_bg_screen_surface.get_rect(center =(SCREEN_CENTER_X, SCREEN_CENTER_Y))

start_button_rect = pygame.Rect(250,485,100,40)
start_quit_button_rect = pygame.Rect(550,485,100,40)

#   instructions
instructions_surface = pygame.image.load("assets/images/UI/instructions.png").convert_alpha()
instructions_rect = instructions_surface.get_rect(center = (SCREEN_CENTER_X, SCREEN_CENTER_Y))

#   credits
credits_surface = pygame.image.load("assets/images/UI/credits.png").convert_alpha()
credits_rect = credits_surface.get_rect(center = (SCREEN_CENTER_X, 600))

# game loop
while True:
    keys = pygame.key.get_pressed()
    moving = False  # reset moving status before checking keys

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == timer_event:
            if game_active: #   time ticks only when the game is running
                time_left -= 1
                
                minutes = time_left // 60
                seconds = time_left % 60
                
                time_left_surface = FONT.render(f"{minutes}:{seconds:02}", True, (255, 255, 255))
                time_left_rect = time_left_surface.get_rect(center = (100,70))

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())  # for checking coordinates
            print(map_offset[0])
            print(map_offset[1])

            #   clicking buttons
            mouse_pos = pygame.mouse.get_pos() 
            
            if game_active:
                
                if ui_bg_showing == False:
                
                    if map_button_rect.collidepoint(mouse_pos) or checklist_button_rect.collidepoint(mouse_pos):
                        ui_bg_showing = True
                    else:
                        ui_bg_showing = False
                
                    if map_button_rect.collidepoint(mouse_pos):
                        print("map clicked")
                        ui_shown = 'map'
                
                    if checklist_button_rect.collidepoint(mouse_pos):
                        print("checklist clicked")
                        ui_shown = 'checklist'
                    
                else:
                
                    if ui_x_rect.collidepoint(mouse_pos):
                        ui_bg_showing = False
                        
            else:            
                if not instructions_showing: #  buttons only work when the start screens showing not while instructions are showing
                    
                    #   start button clicked
                    if start_button_rect.collidepoint(mouse_pos):
                    
                        #   reset game
                        game_over, floor_shown_surface, items_collected, ending, item_list, current_door_list, map_offset, time_left, end_sound_played = reset_game(game_over, floor_shown_surface, items_collected, ending, item_list, current_door_list, map_offset, time_left, end_sound_played)

                        instructions_showing = True                    

                    #   quit button clicked
                    if start_quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

        if event.type == ANIMATION: #   animation
            
            if keys[pygame.K_w]:
                thief_frame = (thief_frame - 1) % 3 
            if keys[pygame.K_s]:
                thief_frame = (thief_frame + 1) % 3 + 6
            if keys[pygame.K_a]:
                thief_frame = (thief_frame + 1) % 3 + 9  
            if keys[pygame.K_d]:
                thief_frame = (thief_frame + 1) % 3 + 3  
                
        if event.type == pygame.KEYDOWN: #  testing floors
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                floor_shown_surface = floor_1_surface
            if keys[pygame.K_2]:
                floor_shown_surface = floor_2_surface
            if keys[pygame.K_3]:
                floor_shown_surface = floor_3_surface
            if keys[pygame.K_SPACE]:
                if game_over:
                    game_active = False
                    game_over = False
                if instructions_showing:
                    game_active = True
                    
    if not channel1.get_busy(): #   so it stops trying to play it over and over every second
        channel1.play(music, loops=-1)
    
    #   if the game's running
    if game_active:

        instructions_showing = False #  instructions can't be displayed while they're playing
        
        #   lose if time's out
        if time_left == 0:
            ending = game_endings[3]
            game_over = True

        if not game_over:
            #   show only the ui when the ui is opened
            if ui_bg_showing:
        
                SCREEN.blit(ui_bg_surface, ui_bg_rect)
        
                SCREEN.blit(ui_x_surface, ui_x_rect)
        
                if ui_shown == 'checklist':
            
                    SCREEN.blit(checklist_surface, checklist_rect)
                    for i in range(no_of_items): #    iterate through the items to check if they're found
                        if item_list[i].found:
                            pygame.draw.rect(SCREEN, CHECKLIST_RED, checklist_list[i])
                    
                if ui_shown == 'map':
            
                    player_location_surface = FONT.render(player_location,True,(0,0,0)) 
                    player_location_rect = player_location_surface.get_rect(center = (SCREEN_CENTER_X,500))
            
                    # map_thief_con_rect = map_thief_icon_surface.get_rect(center = ())
                    for room in room_list:
                        if player_location == room.name:
                            map_thief_con_rect = map_thief_icon_surface.get_rect(center = room.map_coords)

                    # use the current floor to determine which floor is shown on the map ui
                    SCREEN.blit(map_list[current_floor - 1],map_list[current_floor - 1].get_rect(center = (SCREEN_CENTER_X,250)))

                    SCREEN.blit(player_location_surface, player_location_rect)
                    SCREEN.blit(map_thief_icon_surface,map_thief_con_rect)
            
            #   the rest of the game runs while ui is shown so player can't accidentally move while ui is showing
            else:
        
                moving, door_dialogue_surface, door_dialogue_rect, hidden_exit_dialogue_surface, hidden_exit_dialogue_rect, ending, game_over = thief.player_movement(current_wall_list, current_door_list, map_offset, FONT, items_collected, no_of_items, game_endings)
    
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
                elif thief.rect.colliderect(stair_2_down.rect):
                    floor_shown_surface = floor_1_surface
                elif thief.rect.colliderect(left_2_up) or thief.rect.colliderect(right_2_up):
                    floor_shown_surface = floor_3_surface
                elif thief.rect.colliderect(left_3_down) or thief.rect.colliderect(right_3_down):
                    floor_shown_surface = floor_2_surface
            
                #check if any items are found
                for item in item_list:
                    items_collected = item.find_items(map_offset[0],map_offset[1],current_floor, items_collected)
                
                # draw everything
                SCREEN.fill((0, 0, 0))
                SCREEN.blit(floor_shown_surface, floor_rect)
        
                #   walls
                current_wall_list, stair_1_top, stair_2_down, left_2_up, right_2_up, left_3_down, right_3_down = create_walls(Wall, CENTER_OFFSET_X, CENTER_OFFSET_Y, current_floor)
                # draw_walls(current_wall_list, SCREEN, map_offset[0], map_offset[1], current_floor) #get rid of this to make the walls invisible eventually

                #   doors
                current_door_list = create_doors(Door, CENTER_OFFSET_X, CENTER_OFFSET_Y,current_floor)
        
                #   items
                for i in item_list:
                    i.draw_items(map_offset[0], map_offset[1],current_floor)
            
                # unlocking doors and hidden exits
                for door in current_door_list:
                    door.draw_doors(SCREEN,map_offset[0],map_offset[1])
                    door.unlock_hidden_exit(items_collected, no_of_items)
        
                if master_key_item.found and current_floor == 2:
                                current_door_list[0].door_unlock()
                        
                if fire_exit_key_item.found and current_floor == 3:
                        current_door_list[0].door_unlock()
                    
                if door_dialogue_surface and door_dialogue_rect:
                    draw_dialogue(True, SCREEN, door_dialogue_surface, door_dialogue_rect)
                else:
                    draw_dialogue(False, SCREEN, None, None)
            
                if hidden_exit_dialogue_surface and hidden_exit_dialogue_rect:
                    SCREEN.blit(hidden_exit_dialogue_surface, hidden_exit_dialogue_rect)
            
                SCREEN.blit(thief.surface, thief.rect)
                SCREEN.blit(time_left_surface, time_left_rect)
                SCREEN.blit(map_button_surface, map_button_rect)
                SCREEN.blit(checklist_button_surface, checklist_button_rect)
        else:
            #   game end
            if game_over:
                if ending:
                    hidden_exit_dialogue_surface = LARGE_FONT.render(ending,True,(255,255,255))
                    hidden_exit_dialogue_rect = hidden_exit_dialogue_surface.get_rect(center = (SCREEN_CENTER_X, 250))
                    
                    press_space_dialogue_surface = FONT.render("PRESS SPACE TO CONTINUE", True, (255,255,255))
                    press_space_dialogue_rect = press_space_dialogue_surface.get_rect(center = (SCREEN_CENTER_X,500))
                    
                    #   play sound effects
                    #   won
                    if not end_sound_played:
                        if ending == game_endings[0] or ending == game_endings[1] or ending == game_endings[2]:
                            channel2.play(yay)
                        #   lost
                        elif ending == game_endings[3]:
                            channel2.play(siren)
                    
                    end_sound_played = True #   only make sound play once

                    start_bg_screen_rect.centerx -= 1
                    if start_bg_screen_rect.centerx <= - SCREEN_CENTER_X:
                        start_bg_screen_rect.centerx = SCREEN_CENTER_X
            
                    SCREEN.blit(start_bg_screen_surface, start_bg_screen_rect)
                    SCREEN.blit(hidden_exit_dialogue_surface, hidden_exit_dialogue_rect)
                    SCREEN.blit(press_space_dialogue_surface, press_space_dialogue_rect)
    else:
        #   start screen
        hidden_exit_dialogue_surface = None
        hidden_exit_dialogue_rect = None
        
        start_bg_screen_rect.centerx -= 1
        if start_bg_screen_rect.centerx <= - SCREEN_CENTER_X:
            start_bg_screen_rect.centerx = SCREEN_CENTER_X
            
        SCREEN.blit(start_bg_screen_surface, start_bg_screen_rect)
        
        if instructions_showing:
            SCREEN.blit(instructions_surface, instructions_rect)
        else:
            SCREEN.blit(start_screen_surface,start_screen_rect)
            

    pygame.display.update()
    clock.tick(60)  # frame rate
    