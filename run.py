# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
Global variables to be used throughout every room of the game.
"""
weapon = ""
torch_light = 5
inventory = []
score = 0

"""
Nested dictionary containing all the room descriptions, room choices and items.
"""

room_data = {
    'entrance': {
        'description': "Test Description 0",
        'choices': ['1. East', '2. West', '3. Investigate']
    },
    'lower_left': {
        'description': "Test Description 1",
        'choices': ["1. North", "2. East", "3. Investigate"],
    },
    'lower_right': {
        'description': "Test Description 2",
        'choices': ["1. North", "2. West", "3. Investigate"]
    },
    'middle_left': {
        'description': "Test Description 3",
        'choices': ["1. North", "2. East", "3. South", "4. Investigate"]
    },
    'center': {
        'description': "Test Description 4",
        'choices': ["1. fight", "2. Flee"]
    },
    'middle_right': {
        'description': "Test Description 5",
        'choices': ["1. North", "2. South", "3. West", "4. Investigate"]
    },
    'upper_left': {
        'description': "Test Description 6",
        'choices': ["1. East", "2. South", "3. Investigate"]
    },
    'upper_right': {
        'description': "Test Description 7",
        'choices': ["1. South", "2. West", "3. Investigate"]
    },
    'burial_room': {
        'description': "Test Description 8",
        'choices': ["1. North", "2. East", "3. West", "4. Investigate"]
    },
    'antechamber': {
        'description': "Test Description 9",
        'choices': ["1. South", "2. Loot"]
    }
}

"""
Entrance function to handle the first room 
"""

def entrance():
    global torch_light
    run_room = True

    print(room_data['entrance']['description'])

    while run_room:
        print("----------")
        for choice in room_data['entrance']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            lower_left()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            lower_right()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['entrance'].update({'choices':['1. East', '2. West', '3. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
lower_left function to handle the adventure in this room
"""

def lower_left():
    global torch_light
    run_room = True

    print(room_data['lower_left']['description'])

    while run_room:
        print("----------")
        for choice in room_data['lower_left']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            break
        elif entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            entrance()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['lower_left'].update({'choices':['1. North', '2. East', '3. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
lower_right function to handle the adventure in this room
"""

def lower_right():
    global torch_light
    run_room = True

    print(room_data['lower_right']['description'])

    while run_room:
        print("----------")
        for choice in room_data['lower_right']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            break
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            entrance()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['lower_right'].update({'choices':['1. North', '2. West', '3. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
middle_left function to handle the adventure in this room
"""

def middle_left():
    global torch_light
    run_room = True

    print(room_data['middle_left']['description'])

    while run_room:
        print("----------")
        for choice in room_data['middle_left']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            upper_left()
        elif entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            center()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            lower_left()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['middle_left'].update({'choices':['1. North', '2. East', '3. South', '4. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
center function to handle the adventure in this room
"""

def center():
    global torch_light
    run_room = True

    print(room_data['center']['description'])

    while run_room:
        print("----------")
        for choice in room_data['center']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            middle_left()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['center'].update({'choices':['1. East', '2. West', '3. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
middle_right function to handle the adventure in this room
"""

def middle_right():
    global torch_light
    run_room = True

    print(room_data['middle_right']['description'])

    while run_room:
        print("----------")
        for choice in room_data['middle_right']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            upper_right()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            lower_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            center()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['middle_right'].update({'choices':['1. North', '2. South', '3. West', '4. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
upper_left function to handle the adventure in this room
"""

def upper_left():
    global torch_light
    run_room = True

    print(room_data['upper_left']['description'])

    while run_room:
        print("----------")
        for choice in room_data['upper_left']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            burial_room()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            middle_left()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['upper_left'].update({'choices':['1. East', '2. South', '3. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
upper_right function to handle the adventure in this room
"""

def upper_right():
    global torch_light
    run_room = True

    print(room_data['upper_right']['description'])

    while run_room:
        print("----------")
        for choice in room_data['upper_right']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            burial_room()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['upper_right'].update({'choices':['1. South', '2. West', '3. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
burial_room function to handle the adventure in this room
"""

def burial_room():
    global torch_light
    run_room = True

    print(room_data['burial_room']['description'])

    while run_room:
        print("----------")
        for choice in room_data['burial_room']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            antechamber()
        elif entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            upper_left()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            upper_right()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['burial_room'].update({'choices':['1. North', '2. East', '3. West', '4. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
antechamber function to handle the adventure in this room
"""

def antechamber():
    global torch_light
    run_room = True

    print(room_data['antechamber']['description'])

    while run_room:
        print("----------")
        for choice in room_data['antechamber']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            burial_room()
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['antechamber'].update({'choices':['1. South', '2. Investigate (Complete)']})
        else:
            print("Not a valid option, try again!\n")





entrance()