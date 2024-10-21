def create_walls(Wall, center_offset_x, center_offset_y, current_floor):
    # Initialize a dictionary to hold walls for each floor
    wall_list = {
        1: [],
        2: [],
        3: []
        }

    # library
    lib_top = Wall(205 - center_offset_x, 675 - center_offset_y, 655-205, 10, 1)
    wall_list[1].append(lib_top)
    
    lib_right_top = Wall(650 - center_offset_x, 675 - center_offset_y, 10, 850-675, 1)
    wall_list[1].append(lib_right_top)
    
    lib_right_bottom = Wall(650 - center_offset_x, 920 - center_offset_y, 10, 1030-920, 1)
    wall_list[1].append(lib_right_bottom)
    
    lib_bottom = Wall(205 - center_offset_x, 1030 - center_offset_y, 685-205, 10, 1)
    wall_list[1].append(lib_bottom)

    # furniture
    # reading
    lib_couch = Wall(465 - center_offset_x, 820 - center_offset_y, 85, 5, 1)
    wall_list[1].append(lib_couch)
    
    lib_table = Wall(485 - center_offset_x, 880 - center_offset_y, 50, 5, 1)
    wall_list[1].append(lib_table)
    
    lib_stool_1 = Wall(530 - center_offset_x, 940 - center_offset_y, 15, 5, 1)
    wall_list[1].append(lib_stool_1)
    
    lib_stool_2 = Wall(465 - center_offset_x, 940 - center_offset_y, 15, 5, 1)
    wall_list[1].append(lib_stool_2)
    
    lib_shelf = Wall(215 - center_offset_x, 720 - center_offset_y, 655-220, 5, 1)
    wall_list[1].append(lib_shelf)
    
    # desk 
    lib_chair = Wall(465-150 - center_offset_x, 840 - center_offset_y, 40, 5, 1)
    wall_list[1].append(lib_chair)
    
    lib_desk = Wall(280 - center_offset_x, 884 - center_offset_y, 100, 10, 1)
    wall_list[1].append(lib_desk)
    
    lib_plant_top = Wall(280-70 - center_offset_x, 884+90 - center_offset_y, 50, 5, 1)
    wall_list[1].append(lib_plant_top)
    
    lib_plant_right = Wall(260 - center_offset_x, 884+90 - center_offset_y, 5, 50, 1)
    wall_list[1].append(lib_plant_right)

    # dining
    din_top = Wall(210 - center_offset_x, 195 - center_offset_y, 560-205, 10, 1)
    wall_list[1].append(din_top)
    
    din_lib_left = Wall(205 - center_offset_x, 200 - center_offset_y, 10, 1030-200, 1)
    wall_list[1].append(din_lib_left)
    
    din_right_top = Wall(555 - center_offset_x, 195 - center_offset_y, 10, 530-195, 1)
    wall_list[1].append(din_right_top)
    
    din_right_bottom = Wall(555 - center_offset_x, 600 - center_offset_y, 10, 675-600, 1)
    wall_list[1].append(din_right_bottom)

    # furniture
    dining_wall = Wall(210 - center_offset_x, 540-95-115-20-50+5 - center_offset_y, 560-205, 10, 1)
    wall_list[1].append(dining_wall)
    
    dining_chair_1 = Wall(1100-190+5-120-50-180-240 - center_offset_x, 540-95-115-20-50+50+70+50 - center_offset_y, 25, 5, 1)
    wall_list[1].append(dining_chair_1)
    
    dining_table = Wall(1100-190+5-120-50-180-275 - center_offset_x, 540-95-115-20-50+50+70+70 - center_offset_y, 100, 40, 1)
    wall_list[1].append(dining_table)
    
    dining_chair_2 = Wall(1100-190+5-120-50-180-240 - center_offset_x, 540-95-115-20-50+50+70+50+80 - center_offset_y, 25, 5, 1)
    wall_list[1].append(dining_chair_2)

    # cleaning room
    cleaning_right = Wall(780 - center_offset_x, 135 - center_offset_y, 10, 485-135, 1)
    wall_list[1].append(cleaning_right)
    
    cleaning_top = Wall(555 - center_offset_x, 260 - center_offset_y, 785-560, 10, 1)
    wall_list[1].append(cleaning_top)
    
    cleaning_bottom_left = Wall(560 - center_offset_x, 485 - center_offset_y, 640-560, 10, 1)
    wall_list[1].append(cleaning_bottom_left)

    # furniture
    cleaning_wall = Wall(1100-190+5-120-50-180 - center_offset_x, 540-95-115-20-50+50 - center_offset_y, 785-560, 10, 1)
    wall_list[1].append(cleaning_wall)
    
    cleaning_bench_1 = Wall(1100-190+5-120-50-180 - center_offset_x, 540-95-115-20-50+50+70 - center_offset_y, 20, 5, 1)
    wall_list[1].append(cleaning_bench_1)
    
    cleaning_bench_2 = Wall(1100-190+5-120-50-180+120 - center_offset_x, 540-95-115-20-50+50+70 - center_offset_y, 100, 5, 1)
    wall_list[1].append(cleaning_bench_2)

    # kitchen
    kit_cle_bottom = Wall(710 - center_offset_x, 485 - center_offset_y, 1020-710, 10, 1)
    wall_list[1].append(kit_cle_bottom)
    
    kit_bottom_mid = Wall(1090 - center_offset_x, 485 - center_offset_y, 1135-1090, 10, 1)
    wall_list[1].append(kit_bottom_mid)
    
    kit_right_top = Wall(1100 - center_offset_x, 135 - center_offset_y, 10, 265-100, 1)
    wall_list[1].append(kit_right_top)
    
    kit_liv_top = Wall(1100 - center_offset_x, 260 - center_offset_y, 1645-1100, 10, 1)
    wall_list[1].append(kit_liv_top)
    
    kit_bottom_right = Wall(1135 - center_offset_x, 710 - center_offset_y, 1365-1135, 10, 1)
    wall_list[1].append(kit_bottom_right)
    
    kit_left_top = Wall(1130 - center_offset_x, 485 - center_offset_y, 10, 565-485, 1)
    wall_list[1].append(kit_left_top)
    
    kit_top = Wall(780 - center_offset_x, 135 - center_offset_y, 1100-780, 10, 1)
    wall_list[1].append(kit_top)
    
    kit_left_bottom = Wall(1130 - center_offset_x, 630 - center_offset_y, 10, 810-630, 1)
    wall_list[1].append(kit_left_bottom)

    # furniture
    kitchen_island = Wall(1100-190+5 - center_offset_x, 540-95-115-20 - center_offset_y, 90, 5, 1)
    wall_list[1].append(kitchen_island)
    
    fridge = Wall(1100-190+5-120 - center_offset_x, 540-95-115-20-50 - center_offset_y, 40, 40, 1)
    wall_list[1].append(fridge)
    
    kitchen_wall = Wall(1100-190+5-120-10 - center_offset_x, 540-95-115-20-50-60 - center_offset_y, 1100-780, 10, 1)
    wall_list[1].append(kitchen_wall)

    # living area
    living_left_top = Wall(1355 - center_offset_x, 265 - center_offset_y, 10, 715-265, 1)
    wall_list[1].append(living_left_top)
    
    living_left_bottom = Wall(1130 - center_offset_x, 965 - center_offset_y, 10, 1030-965, 1)
    wall_list[1].append(living_left_bottom)
    
    living_right = Wall(1645 - center_offset_x, 265 - center_offset_y, 10, 1030-265, 1)
    wall_list[1].append(living_right)
    
    living_bottom = Wall(1105 - center_offset_x, 1030 - center_offset_y, 1645-1105, 10, 1)
    wall_list[1].append(living_bottom)

    # furniture
    living_paintings = Wall(1130 - center_offset_x, 740 - center_offset_y, 1360-1130, 5, 1)
    wall_list[1].append(living_paintings)
    
    fire_couch = Wall(1510 - center_offset_x, 680 - center_offset_y, 105, 10, 1)
    wall_list[1].append(fire_couch)
    
    fireplace = Wall(1510 - center_offset_x, 540 - center_offset_y, 95, 40, 1)
    wall_list[1].append(fireplace)
    
    tv_couch = Wall(1510-60 - center_offset_x, 540-95 - center_offset_y, 105, 10, 1)
    wall_list[1].append(tv_couch)
    
    tv_wall = Wall(1100 - center_offset_x, 540-95-115 - center_offset_y, 1645-1100, 5, 1)
    wall_list[1].append(tv_wall)
    
    tv = Wall(1455 - center_offset_x, 330 - center_offset_y, 100, 10, 1)
    wall_list[1].append(tv)

    # conversation pit
    conversation_pit_top = Wall(1360 - center_offset_x, 840 - center_offset_y, 250, 5, 1)
    wall_list[1].append(conversation_pit_top)
    
    conversation_pit_left = Wall(1360 - center_offset_x, 915 - center_offset_y, 5, 55, 1)
    wall_list[1].append(conversation_pit_left)
    
    conversation_pit_stair = Wall(1360 - center_offset_x, 915 - center_offset_y, 25, 5, 1)
    wall_list[1].append(conversation_pit_stair)
    
    conversation_pit_bottom = Wall(1360 - center_offset_x, 970 - center_offset_y, 250, 5, 1)
    wall_list[1].append(conversation_pit_bottom)
    
    conversation_pit_right = Wall(1610 - center_offset_x, 840 - center_offset_y, 5, 130, 1)
    wall_list[1].append(conversation_pit_right)
    
    con_table = Wall(1450 - center_offset_x, 900 - center_offset_y, 80, 5, 1)
    wall_list[1].append(con_table)
    
    con_chair = Wall(1590 - center_offset_x, 880 - center_offset_y, 15, 5, 1)
    wall_list[1].append(con_chair)

    # foyer
    foyer_left = Wall(685 - center_offset_x, 1030 - center_offset_y, 10, 1160-1030, 1)
    wall_list[1].append(foyer_left)
    
    foyer_right = Wall(1105 - center_offset_x, 1030 - center_offset_y, 10, 1160-1030, 1)
    wall_list[1].append(foyer_right)
    
    foyer_bottom_left = Wall(685 - center_offset_x, 1160 - center_offset_y, 860-685, 10, 1)
    wall_list[1].append(foyer_bottom_left)
    
    foyer_bottom_right = Wall(925 - center_offset_x, 1160 - center_offset_y, 1105-925, 10, 1)
    wall_list[1].append(foyer_bottom_right)

    # stair walls
    stair_1_left = Wall(800 - center_offset_x, 485 - center_offset_y, 10, 725-485, 1)
    wall_list[1].append(stair_1_left)
    
    stair_1_right = Wall(960 - center_offset_x, 485 - center_offset_y, 10, 725-485, 1)
    wall_list[1].append(stair_1_right)
    
    stair_1_top = Wall(800 - center_offset_x, 490 - center_offset_y, 160, 10, 1)
    wall_list[1].append(stair_1_top)

    return wall_list[current_floor], stair_1_top
