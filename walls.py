def create_walls(Wall, center_offset_x, center_offset_y):
  wall_list = []

  #library
  lib_top = wall_list.append(Wall(205 - center_offset_x, 675 - center_offset_y, 655-205, 10))
  lib_right_top = wall_list.append(Wall(650 - center_offset_x, 675 - center_offset_y, 10, 850-675))
  lib_right_bottom = wall_list.append(Wall(650 - center_offset_x, 920 - center_offset_y, 10, 1030-920))
  lib_bottom = wall_list.append(Wall(205 - center_offset_x, 1030 - center_offset_y, 685-205, 10))
  #       furniture
  #                       reading
  lib_couch = wall_list.append(Wall(465 - center_offset_x,820 - center_offset_y, 85, 5))
  lib_table = wall_list.append(Wall(485 - center_offset_x,880 - center_offset_y, 50,5))
  lib_stool_1 = wall_list.append(Wall(530 - center_offset_x, 940 - center_offset_y, 15, 5))
  lib_stool_2 = wall_list.append(Wall(465 - center_offset_x, 940 - center_offset_y, 15, 5))
  lib_shelf = wall_list.append(Wall(215 - center_offset_x, 720 - center_offset_y,655-220, 5))
  #                       desk 
  lib_chair = wall_list.append(Wall(465-150 - center_offset_x, 840 - center_offset_y, 40, 5))
  lib_desk = wall_list.append(Wall(280 - center_offset_x, 884 - center_offset_y, 100, 10))
  lib_plant_top = wall_list.append(Wall(280-70 - center_offset_x, 884+90 - center_offset_y, 50, 5))
  lib_plant_right = wall_list.append(Wall(260 - center_offset_x, 884+90 - center_offset_y, 5, 50))
  
  
  #dining
  din_top = wall_list.append(Wall(210 - center_offset_x, 195 - center_offset_y, 560-205, 10))
  din_lib_left = wall_list.append(Wall(205 - center_offset_x, 200 - center_offset_y, 10, 1030-200))
  din_right_top = wall_list.append(Wall(555 - center_offset_x, 195 - center_offset_y, 10, 530-195))
  din_right_bottom = wall_list.append(Wall(555 - center_offset_x, 600 - center_offset_y, 10, 675-600))
  #       furniture
  dining_wall = wall_list.append(Wall(210 - center_offset_x, 540-95-115-20-50+5 - center_offset_y, 560-205, 10))
  dining_chair_1 = wall_list.append(Wall(1100-190+5-120-50-180-240 - center_offset_x,540-95-115-20-50+50+70+50 - center_offset_y, 25,5))
  dining_table = wall_list.append(Wall(1100-190+5-120-50-180-275 - center_offset_x,540-95-115-20-50+50+70+70 - center_offset_y, 100,40))
  dining_chair_2 = wall_list.append(Wall(1100-190+5-120-50-180-240 - center_offset_x,540-95-115-20-50+50+70+50+80 - center_offset_y, 25,5))
  
  
  #cleaning room
  cleaning_right = wall_list.append(Wall(780 - center_offset_x, 135 - center_offset_y, 10, 485-135))
  cleaning_top = wall_list.append(Wall(555 - center_offset_x, 260 - center_offset_y, 785-560, 10))
  cleaning_bottom_left = wall_list.append(Wall(560 - center_offset_x, 485 - center_offset_y, 640-560, 10))
  #       furniture
  cleaning_wall = wall_list.append(Wall(1100-190+5-120-50-180 - center_offset_x,540-95-115-20-50+50 - center_offset_y, 785-560,10))
  cleaning_bench_1 = wall_list.append(Wall(1100-190+5-120-50-180 - center_offset_x,540-95-115-20-50+50+70 - center_offset_y, 20,5))
  cleaning_bench_2 = wall_list.append(Wall(1100-190+5-120-50-180+120 - center_offset_x,540-95-115-20-50+50+70 - center_offset_y, 100,5))
  
  
  #kitchen
  kit_cle_bottom = wall_list.append(Wall(710 - center_offset_x, 485 - center_offset_y, 1020-710, 10))
  kit_bottom_mid = wall_list.append(Wall(1090 - center_offset_x, 485 - center_offset_y, 1135-1090, 10))
  kit_right_top = wall_list.append(Wall(1100 - center_offset_x, 135 - center_offset_y, 10, 265-100))
  kit_liv_top = wall_list.append(Wall(1100 - center_offset_x, 260 - center_offset_y, 1645-1100, 10))
  kit_bottom_right = wall_list.append(Wall(1135 - center_offset_x, 710 - center_offset_y, 1365-1135, 10))
  kit_left_top = wall_list.append(Wall(1130 - center_offset_x, 485 - center_offset_y, 10, 565-485))
  kit_top = wall_list.append(Wall(780 - center_offset_x, 135 - center_offset_y, 1100-780,10))
  kit_left_bottom = wall_list.append(Wall(1130 - center_offset_x, 630 - center_offset_y, 10, 810-630))
  #       furniture
  kitchen_island = wall_list.append(Wall(1100-190+5 - center_offset_x, 540-95-115-20 - center_offset_y, 90, 5))
  fridge = wall_list.append(Wall(1100-190+5-120 - center_offset_x,540-95-115-20-50 - center_offset_y, 40, 40))
  kitchen_wall = wall_list.append(Wall(1100-190+5-120-10 - center_offset_x, 540-95-115-20-50-60 - center_offset_y,1100-780,10))
  
  
  #living area
  living_left_top = wall_list.append(Wall(1355 - center_offset_x, 265 - center_offset_y, 10, 715-265))
  living_left_bottom = wall_list.append(Wall(1130 - center_offset_x, 965 - center_offset_y, 10, 1030-965))
  living_right = wall_list.append(Wall(1645 - center_offset_x, 265 - center_offset_y, 10, 1030-265))
  living_bottom = wall_list.append(Wall(1105 - center_offset_x, 1030 - center_offset_y, 1645-1105, 10))
  #       furniture
  living_paintings = wall_list.append(Wall(1130 - center_offset_x, 740 - center_offset_y, 1360-1130, 5))
  fire_couch = wall_list.append(Wall(1510 - center_offset_x, 680 - center_offset_y, 105, 10))
  fireplace = wall_list.append(Wall(1510 - center_offset_x, 540 - center_offset_y, 95, 40))
  tv_couch = wall_list.append(Wall(1510-60 - center_offset_x, 540-95 - center_offset_y, 105, 10))
  tv_wall = wall_list.append(Wall(1100 - center_offset_x, 540-95-115 - center_offset_y, 1645-1100,5))
  tv = Wall(1455 - center_offset_x,330 - center_offset_y, 100, 10)
  wall_list.append(tv)
  #                   conversation pit
  conversation_pit_top = wall_list.append(Wall(1360 - center_offset_x, 840 - center_offset_y, 250, 5))
  conversation_pit_left = wall_list.append(Wall(1360 - center_offset_x, 915 - center_offset_y, 5, 55))
  conversation_pit_stair = wall_list.append(Wall(1360 - center_offset_x, 915 - center_offset_y, 25, 5))
  conversation_pit_bottom = wall_list.append(Wall(1360 - center_offset_x, 970 - center_offset_y, 250, 5))
  conversation_pit_right = wall_list.append(Wall(1610 - center_offset_x, 840 - center_offset_y, 5, 130))
  con_table = wall_list.append(Wall(1450 - center_offset_x, 900 - center_offset_y, 80, 5))
  con_chair = wall_list.append(Wall(1590 - center_offset_x, 880 - center_offset_y, 15, 5))
  
  
  #foyer
  foyer_left = wall_list.append(Wall(685 - center_offset_x, 1030 - center_offset_y, 10, 1160-1030))
  foyer_right = wall_list.append(Wall(1105 - center_offset_x, 1030 - center_offset_y, 10, 1160-1030))
  foyer_bottom_left = wall_list.append(Wall(685 - center_offset_x, 1160 - center_offset_y, 860-685, 10))
  foyer_bottom_right = wall_list.append(Wall(925 - center_offset_x, 1160 - center_offset_y, 1105-925, 10))
  
  #stair walls
  stair_1_left = wall_list.append(Wall(800 - center_offset_x, 485 - center_offset_y, 10, 725-485))
  stair_1_right = wall_list.append(Wall(960 - center_offset_x, 485 - center_offset_y, 10, 725-485))

  return wall_list
