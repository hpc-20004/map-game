def create_walls(Wall, cx, cy, current_floor):
    # Initialize a dictionary to hold walls for each floor
    wall_list = {
        1: [],
        2: [],
        3: []
        }

    # Floor 1
    # library
    lib_top = Wall(205 - cx, 675 - cy, 655-205, 10)
    wall_list[1].append(lib_top)
    
    lib_right_top = Wall(650 - cx, 675 - cy, 10, 850-695)
    wall_list[1].append(lib_right_top)
    
    lib_right_bottom = Wall(650 - cx, 920 - cy, 10, 1030-920)
    wall_list[1].append(lib_right_bottom)
    
    lib_bottom = Wall(205 - cx, 1030 - cy, 685-205, 10)
    wall_list[1].append(lib_bottom)

    # furniture
    # reading
    lib_couch = Wall(465 - cx, 820 - cy, 85, 5)
    wall_list[1].append(lib_couch)
    
    lib_table = Wall(485 - cx, 880 - cy, 50, 5)
    wall_list[1].append(lib_table)
    
    lib_stool_1 = Wall(530 - cx, 940 - cy, 15, 5)
    wall_list[1].append(lib_stool_1)
    
    lib_stool_2 = Wall(465 - cx, 940 - cy, 15, 5)
    wall_list[1].append(lib_stool_2)
    
    lib_shelf = Wall(215 - cx, 720 - cy, 655-220, 5)
    wall_list[1].append(lib_shelf)
    
    # desk 
    lib_chair = Wall(465-150 - cx, 840 - cy, 40, 5)
    wall_list[1].append(lib_chair)
    
    lib_desk = Wall(280 - cx, 884 - cy, 100, 10)
    wall_list[1].append(lib_desk)
    
    lib_plant_top = Wall(280-70 - cx, 884+90 - cy, 50, 5)
    wall_list[1].append(lib_plant_top)
    
    lib_plant_right = Wall(260 - cx, 884+90 - cy, 5, 50)
    wall_list[1].append(lib_plant_right)

    # dining
    din_top = Wall(210 - cx, 195 - cy, 560-205, 10)
    wall_list[1].append(din_top)
    
    din_lib_left = Wall(205 - cx, 200 - cy, 10, 1030-200)
    wall_list[1].append(din_lib_left)
    
    din_right_top = Wall(555 - cx, 195 - cy, 10, 530-195)
    wall_list[1].append(din_right_top)
    
    din_right_bottom = Wall(555 - cx, 600 - cy, 10, 675-600)
    wall_list[1].append(din_right_bottom)

    # furniture
    dining_wall = Wall(210 - cx, 540-95-115-20-50+5 - cy, 560-205, 10)
    wall_list[1].append(dining_wall)
    
    dining_chair_1 = Wall(1100-190+5-120-50-180-240 - cx, 540-95-115-20-50+50+70+50 - cy, 25, 5)
    wall_list[1].append(dining_chair_1)
    
    dining_table = Wall(1100-190+5-120-50-180-275 - cx, 540-95-115-20-50+50+70+70 - cy, 100, 40)
    wall_list[1].append(dining_table)
    
    dining_chair_2 = Wall(1100-190+5-120-50-180-240 - cx, 540-95-115-20-50+50+70+50+80 - cy, 25, 5)
    wall_list[1].append(dining_chair_2)

    # cleaning room
    cleaning_right = Wall(780 - cx, 135 - cy, 10, 485-135)
    wall_list[1].append(cleaning_right)
    
    cleaning_top = Wall(555 - cx, 260 - cy, 785-560, 10)
    wall_list[1].append(cleaning_top)
    
    cleaning_bottom_left = Wall(560 - cx, 485 - cy, 640-560, 10)
    wall_list[1].append(cleaning_bottom_left)

    # furniture
    cleaning_wall = Wall(1100-190+5-120-50-180 - cx, 540-95-115-20-50+50 - cy, 785-560, 10)
    wall_list[1].append(cleaning_wall)
    
    cleaning_bench_1 = Wall(1100-190+5-120-50-180 - cx, 540-95-115-20-50+50+70 - cy, 20, 5)
    wall_list[1].append(cleaning_bench_1)
    
    cleaning_bench_2 = Wall(1100-190+5-120-50-180+120 - cx, 540-95-115-20-50+50+70 - cy, 100, 5)
    wall_list[1].append(cleaning_bench_2)

    # kitchen
    kit_cle_bottom = Wall(710 - cx, 485 - cy, 1020-710, 10)
    wall_list[1].append(kit_cle_bottom)
    
    kit_bottom_mid = Wall(1090 - cx, 485 - cy, 1135-1090, 10)
    wall_list[1].append(kit_bottom_mid)
    
    kit_right_top = Wall(1100 - cx, 135 - cy, 10, 265-100)
    wall_list[1].append(kit_right_top)
    
    kit_liv_top = Wall(1100 - cx, 260 - cy, 1645-1100, 10)
    wall_list[1].append(kit_liv_top)
    
    kit_bottom_right = Wall(1135 - cx, 710 - cy, 1365-1135, 10)
    wall_list[1].append(kit_bottom_right)
    
    kit_left_top = Wall(1130 - cx, 485 - cy, 10, 565-485)
    wall_list[1].append(kit_left_top)
    
    kit_top = Wall(780 - cx, 135 - cy, 1100-780, 10)
    wall_list[1].append(kit_top)
    
    kit_left_bottom = Wall(1130 - cx, 630 - cy, 10, 810-630)
    wall_list[1].append(kit_left_bottom)

    # furniture
    kitchen_island = Wall(1100-190+5 - cx, 540-95-115-20 - cy, 90, 5)
    wall_list[1].append(kitchen_island)
    
    fridge = Wall(1100-190+5-120 - cx, 540-95-115-20-50 - cy, 40, 40)
    wall_list[1].append(fridge)
    
    kitchen_wall = Wall(1100-190+5-120-10 - cx, 540-95-115-20-50-60 - cy, 1100-780, 10)
    wall_list[1].append(kitchen_wall)

    # living area
    living_left_top = Wall(1355 - cx, 265 - cy, 10, 715-265)
    wall_list[1].append(living_left_top)
    
    living_left_bottom = Wall(1130 - cx, 965 - cy, 10, 1030-965)
    wall_list[1].append(living_left_bottom)
    
    living_right = Wall(1645 - cx, 265 - cy, 10, 1030-265)
    wall_list[1].append(living_right)
    
    living_bottom = Wall(1105 - cx, 1030 - cy, 1645-1105, 10)
    wall_list[1].append(living_bottom)

    # furniture
    living_paintings = Wall(1130 - cx, 740 - cy, 1360-1130, 5)
    wall_list[1].append(living_paintings)
    
    fire_couch = Wall(1510 - cx, 680 - cy, 105, 10)
    wall_list[1].append(fire_couch)
    
    fireplace = Wall(1510 - cx, 540 - cy, 95, 40)
    wall_list[1].append(fireplace)
    
    tv_couch = Wall(1510-60 - cx, 540-95 - cy, 105, 10)
    wall_list[1].append(tv_couch)
    
    tv_wall = Wall(1100 - cx, 540-95-115 - cy, 1645-1100, 5)
    wall_list[1].append(tv_wall)
    
    tv = Wall(1455 - cx, 330 - cy, 100, 10)
    wall_list[1].append(tv)

    # conversation pit
    conversation_pit_top = Wall(1360 - cx, 840 - cy, 250, 5)
    wall_list[1].append(conversation_pit_top)
    
    conversation_pit_left = Wall(1360 - cx, 915 - cy, 5, 55)
    wall_list[1].append(conversation_pit_left)
    
    conversation_pit_stair = Wall(1360 - cx, 915 - cy, 25, 5)
    wall_list[1].append(conversation_pit_stair)
    
    conversation_pit_bottom = Wall(1360 - cx, 970 - cy, 250, 5)
    wall_list[1].append(conversation_pit_bottom)
    
    conversation_pit_right = Wall(1610 - cx, 840 - cy, 5, 130)
    wall_list[1].append(conversation_pit_right)
    
    con_table = Wall(1450 - cx, 900 - cy, 80, 5)
    wall_list[1].append(con_table)
    
    con_chair = Wall(1590 - cx, 880 - cy, 15, 5)
    wall_list[1].append(con_chair)

    # foyer
    foyer_left = Wall(685 - cx, 1030 - cy, 10, 1160-1030)
    wall_list[1].append(foyer_left)
    
    foyer_right = Wall(1105 - cx, 1030 - cy, 10, 1160-1030)
    wall_list[1].append(foyer_right)
    
    foyer_bottom_left = Wall(685 - cx, 1160 - cy, 860-685, 10)
    wall_list[1].append(foyer_bottom_left)
    
    foyer_bottom_right = Wall(925 - cx, 1160 - cy, 1105-925, 10)
    wall_list[1].append(foyer_bottom_right)

    # stair walls
    stair_1_left = Wall(800 - cx, 485 - cy, 10, 725-485)
    wall_list[1].append(stair_1_left)
    
    stair_1_right = Wall(960 - cx, 485 - cy, 10, 725-485)
    wall_list[1].append(stair_1_right)
    
    stair_1_top = Wall(800 - cx, 490 - cy, 160, 10)
    wall_list[1].append(stair_1_top)
    
    # Floor 2
    # stair down walls
    stair_2_down = Wall(800 - cx, 490+725-485 - cy, 170, 10)
    wall_list[2].append(stair_2_down)
    
    stair_2_top_left_railing = Wall(800-50 - cx, 490+725-485-210 - cy,50,10)
    wall_list[2].append(stair_2_top_left_railing)
    
    stair_2_top_right_railing = Wall(800-50+160+50 - cx, 490+725-485-210 - cy,50,10)
    wall_list[2].append(stair_2_top_right_railing)
    
    stair_2_left_railing = Wall(750 - cx, 520 - cy, 10, 730-520+90)
    wall_list[2].append(stair_2_left_railing)
    
    stair_2_right_railing = Wall(1010 - cx, 520 - cy, 10, 730-520+90)
    wall_list[2].append(stair_2_right_railing)
    
    stair_2_bottom_railing = Wall(750 - cx, 820 - cy, 270, 10)
    wall_list[2].append(stair_2_bottom_railing)
    
    stair_2_down_left = Wall(800 - cx, 520 - cy, 10, 210)
    wall_list[2].append(stair_2_down_left)
    
    stair_2_down_right = Wall(960 - cx, 520 - cy, 10, 210)
    wall_list[2].append(stair_2_down_right)
    
    #master bedroom
    #walls
    master_right_top = Wall(750-260 - cx, 520+35 - cy, 10, 135)
    wall_list[2].append(master_right_top)
    
    master_right_bottom = Wall(750-260 - cx, 520+35+75+140 - cy, 10, 260)
    wall_list[2].append(master_right_bottom)
    
    
    #ensuite
    ensuite_left = Wall(205 - cx, 650 - cy, 45, 40)
    wall_list[2].append(ensuite_left)
    
    ensuite_right = Wall(330 - cx, 650 - cy, 45, 40)
    wall_list[2].append(ensuite_right)
    
    ensuite_side = Wall(365 - cx, 555 - cy, 10, 95)
    wall_list[2].append(ensuite_side)
    
    #bedroom 2
    #walls
    bedroom_2_bottom = Wall(205 - cx, 555 - cy, 390, 40)
    wall_list[2].append(bedroom_2_bottom)
    
    bedroom_2_right_top = Wall(585 - cx, 135 - cy, 10, 270)
    wall_list[2].append(bedroom_2_right_top)
    
    bedroom_2_right_bottom = Wall(585 - cx, 555-80 - cy, 10, 80)
    wall_list[2].append(bedroom_2_right_bottom)
    
    #powder room
    #walls
    powder_room_bottom = Wall(585 - cx, 260 - cy, 190, 40)
    wall_list[2].append(powder_room_bottom)

    powder_room_right_bottom = Wall(775 - cx, 235 - cy, 10, 50)
    wall_list[2].append(powder_room_right_bottom)
    
    #bathroom
    #walls
    bathroom_left_top = Wall(815+190 - cx, 135 - cy, 10, 80)
    wall_list[2].append(bathroom_left_top)
    
    bathroom_left_bottom = Wall(815+190 - cx, 290 - cy, 10, 80)
    wall_list[2].append(bathroom_left_bottom)
    
    bathroom_bottom = Wall(815+190 - cx, 360 - cy, 290, 40)
    wall_list[2].append(bathroom_bottom)
    
    #bedroom 3
    #walls
    bedroom_3_left_top = Wall(1105+190 - cx, 135 - cy, 10, 360-135+100-20)
    wall_list[2].append(bedroom_3_left_top)
    
    bedroom_3_4_left = Wall(1295 - cx, 515 - cy, 10, 215)
    wall_list[2].append(bedroom_3_4_left) 
    
    #bedroom 4
    #walls
    bedroom_4_top = Wall(1295 -cx, 580 - cy, 350, 40)
    wall_list[2].append(bedroom_4_top)
    
    bedroom_4_left = Wall(1295 - cx, 800 -cy, 10, 230)
    wall_list[2].append(bedroom_4_left)

    #outside walls
    floor_2_bottom = Wall(205 - cx, 1030 - cy, 1645-210, 10)
    wall_list[2].append(floor_2_bottom)
    
    floor_2_top = Wall(205 - cx, 135 - cy, 1645-210, 40)
    wall_list[2].append(floor_2_top)
    
    floor_2_left = Wall(205 - cx, 135 - cy, 10, 1030-135)
    wall_list[2].append(floor_2_left)
    
    floor_2_right = Wall(1645 - cx, 135 - cy, 10, 1030-135)
    wall_list[2].append(floor_2_right)
    
    #stair up walls
    invisible_railing_2 = Wall(580 - cx, 920 - cy, 590, 10)
    wall_list[2].append(invisible_railing_2)
    
    left_2_up = Wall(830 - cx, 920 - cy, 10,100)
    wall_list[2].append(left_2_up)
    
    right_2_up = Wall(920 - cx, 920 - cy, 10, 100)
    wall_list[2].append(right_2_up)
    
    # Floor 3
    # stair walls
    stair_3_left_railing = Wall(580 - cx, 920 - cy, 250, 10)
    wall_list[3].append(stair_3_left_railing)
    
    stair_3_right_railing = Wall(920 - cx, 920 - cy, 250, 10)
    wall_list[3].append(stair_3_right_railing)
    
    left_3_down = Wall(580 - cx, 920 - cy, 10, 100)
    wall_list[3].append(left_3_down)
    
    right_3_down = Wall(1170 - cx, 920 - cy, 10, 100)
    wall_list[3].append(right_3_down)
    
    # art gallery
    # walls
    art_top_left = Wall(495 - cx, 425 - cy, 105, 40)
    wall_list[3].append(art_top_left)
    
    art_top_right = Wall(675 - cx, 425 - cy, 815-675, 40)
    wall_list[3].append(art_top_right)
    
    # vault
    # walls
    vault_mus = Wall(815 - cx, 135 - cy, 10, 335)
    wall_list[3].append(vault_mus)
    
    # music room
    # walls 
    mus_left = Wall(815 - cx, 540 - cy, 10, 40)
    wall_list[3].append(mus_left)

    mus_bottom = Wall(815 - cx, 580 - cy, 1295-815, 40)
    wall_list[3].append(mus_bottom)
    
    # fire exit
    # walls
    fire_left = Wall(1165 - cx, 135 - cy, 10, 260-135)
    wall_list[3].append(fire_left)
    
    # fire_bottom = Wall(1165 - cx, 260 - cy, 1295, 40)
    # wall_list[3].append(fire_bottom)
    
    
    # outside walls
    floor_3_top = Wall(495 - cx, 135 - cy, 1295-495, 40)
    wall_list[3].append(floor_3_top)
    
    floor_3_right = Wall(1295 - cx, 135 - cy, 10, 1030-135)
    wall_list[3].append(floor_3_right)
    
    floor_3_bottom = Wall(495 - cx, 1030 - cy, 1295-495, 10)
    wall_list[3].append(floor_3_bottom)
    
    floor_3_left = Wall(495 - cx, 135 - cy, 10, 1030-135)
    wall_list[3].append(floor_3_left)

    return wall_list[current_floor], stair_1_top, stair_2_down, left_2_up, right_2_up, left_3_down, right_3_down
