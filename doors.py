def create_doors(Door, cx, cy,current_floor):
    door_list = {
        1: [],
        2: [],
        3: []
        }
    
    #   Floor 1
    cleaning_door = Door("Cleaning Closet",640 - cx, 485 - cy, 70, 80, False, False, 'vertical')
    door_list[1].append(cleaning_door)
    
    front_door = Door("Front Door", 850 - cx, 1160 - cy, 10, 85, True, True, 'vertical')
    door_list[1].append(front_door)

    #   Floor 2
    master_door = Door("Master Bedroom",490 - cx, 690 - cy, 75, 10, True, False, 'horizontal')
    door_list[2].append(master_door)
    
    powder_window = Door("Powder Room Window", 720 - cx, 155 - cy, 30, 40, True, True, 'vertical')
    door_list[2].append(powder_window)
    
    #   Floor 3
    fire_door = Door("Fire Exit", 1210 - cx, 270 - cy, 70, 40, True, True, 'vertical')
    door_list[3].append(fire_door)
    
    return door_list[current_floor]