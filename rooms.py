def create_rooms(Room):
    #   Room list
    room_list = []

    # Floor 1
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
    master = Room("Master Bedroom",400,635,-50,335,2,True,False)
    room_list.append(master)
    
    ensuite = Room("Ensuite",510,640,300,375,2,False,False)
    room_list.append(ensuite)
    
    hallway = Room("Hallway",-405,350,-50,755,2,False,False)
    room_list.append(hallway)
    
    powder_room = Room("Powder Room",115,255,720,755,2,False,False)
    room_list.append(powder_room)
    
    bathroom = Room("Bathroom",-405,-165,620,755,2,False,False)
    room_list.append(bathroom)
    
    room_2 = Room("Bedroom 2",305,635,425,755,2,False,False)
    room_list.append(room_2)
    
    room_3 = Room("Bedroom 3",-755,-455,400,755,2,False,False)
    room_list.append(room_3)
    
    room_4 = Room("Bedroom 4",-755,-455,-50,310,2,False,False)
    room_list.append(room_4)
    
    #   Floor 3
    art = Room("Art Gallery",-405,345,-50,465,3,False,False)
    room_list.append(art)
    
    vault = Room("Vault",75,345,555,755,3,False,False)
    room_list.append(vault)
    
    music = Room("Music Room",-405,25,400,755,3,False,False)
    room_list.append(music)
    
    return room_list
