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

    run_game = True

    while run_game:
        print(room_data['entrance']['description'])
        print("----------")
        for choice in room_data['entrance']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            break
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            break
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['entrance'].update({'choices':['1. East', '2. West', '3. Investigate (Complete)']})
        else:
            print("Not a valid option\n")




entrance()