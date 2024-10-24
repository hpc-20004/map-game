def create_doors(Door, cx, cy,current_floor):
    door_list = {
        1: [],
        2: [],
        3: []
        }
    
    cleaning_door = Door(640 - cx, 485 - cy, 70, 80, False,False, 'vertical')
    door_list[1].append(cleaning_door)

    master_door = Door(490 - cx, 690 - cy, 75, 10, True, False, 'horizontal')
    door_list[2].append(master_door)
    
    
    
    return door_list[current_floor]