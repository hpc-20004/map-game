def create_doors(Door, cx, cy,current_floor):
    door_list = {
        1: [],
        2: [],
        3: []
        }
    
    cleaning_door = Door("Cleaning Closet",640 - cx, 485 - cy, 70, 80, False, False, 'vertical')
    door_list[1].append(cleaning_door)

    master_door = Door("Master Bedroom",490 - cx, 690 - cy, 75, 10, True, False, 'horizontal')
    door_list[2].append(master_door)
    
    fire_door = Door("Fire Exit", 1210 - cx, 270 - cy, 70, 40, True, True, 'vertical')
    door_list[3].append(fire_door)
    
    return door_list[current_floor]