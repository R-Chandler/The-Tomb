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
        'description': "As you cross the threshold to the tomb and move cautiously down the stone stairs you feel a stone shift under your foot making a soft click. Suddenly the door behind you slams shut with a loud crash. In the pitch darkness you light a torch and as your eyes adjust to the new gloom you see two doors leading deeper into the tomb.",
        'choices': ['1. East', '2. West', '3. Search']
    },
    'lower_left': {
        'description': "A low hiss greets you as you step through the threshold. Coiled serpent motifs adorn the walls, their eyes gleaming with a sense of knowing. A winding path leads deeper into the chamber, guarded by stone snake statues that seem to slither in the shadows. The air is cool and filled with a faint aroma of ancient oils. In the center lies a mysterious pool reflecting the glow of a lone, suspended orb.",
        'choices': ["1. North", "2. East", "3. Search"],
    },
    'lower_right': {
        'description': "As you enter the Chamber of Eternal Flames, a warm gust of air tinged with the scent of burning incense envelops you. Torches flicker with an ethereal flame, casting dancing shadows on the crimson walls adorned with depictions of phoenixes and fiery serpents. In the center, a brazier burns with an unquenchable fire.",
        'choices': ["1. North", "2. West", "3. Search"]
    },
    'middle_left': {
        'description': "In this new room a mysterious darkness cloaks the space. Dimly lit torches barely pierce the gloom, revealing walls adorned with intricate shadow play. The air is thick with ancient incense. Silhouettes seem to dance along the walls as you move with the torch. You get the unnerving feeling that you are being watched, a crashing sound comes from the eastern passage.",
        'choices': ["1. North", "2. East", "3. South", "4. Search"]
    },
    'center': {
        'description': "You cautiously step into what seems like a crypt, the air becomes thick and oppressive. The walls are adorned with carvings of Ammit, a monstrous amalgamation of lion, hippopotamus, and crocodile. Eerie whispers echo through the chamber, and a growl rumbles in the shadows. In the center of the room lies an ancient altar, upon which rests a forbidden relic. As you step towards the altar a shadowed figure slowly climbs onto it, showing you its many razor teeth in your torch light with a snarl.",
        'choices': ["1. fight", "2. Flee"]
    },
    'middle_right': {
        'description': "Upon entering the Chamber, an uncanny silence blankets the room. The walls are adorned with faded murals portraying courtly intrigues and secrets of the ancient kingdom. Hieroglyphic whispers seem to emerge from the very stone, telling tales of conspiracies and hidden truths. A central dais holds an ancient throne. Upon the throne sits an armour clad statue, in his outstretched hands something metal glimmers in the soft torch light. A muffled groan emanates from the western passageway.",
        'choices': ["1. North", "2. South", "3. West", "4. Search"]
    },
    'upper_left': {
        'description': "As you step into the chamber the scent of ancient parchment fills your nostrils, your torchlight flickers across the walls revealing that every inch is covered in hieroglyphs, telling tales of conquests and rituals that have long been forgotten. An ominous statue stands at the north end of the room.",
        'choices': ["1. East", "2. South", "3. Search"]
    },
    'upper_right': {
        'description': "Entering this grand hall you notice your footsteps are louder, echoing around the immense room. The walls are lined with large statues of Anubis, the eyes of the jackal headed god seem to follow your every move. A pedestal standing atop a small staircase at the far end of the room catches your attention.",
        'choices': ["1. South", "2. West", "3. Search"]
    },
    'burial_room': {
        'description': "This is it! You have found the room that has eluded archaeologists for centuries. You find yourself standing in the burial chamber of the tomb, the walls are plastered with gold and jewels. Great stone tablets stand against the eastern wall with stories carved into them depicting the great deeds of the fallen pharaoh. Looking to the north you see the grand sarcophagus standing in the middle of the room, protection spells are engraved along the seal, they seem to glow and then you notice it… a beam of light is shining upon the lid coming from an open shaft on the ceiling… Could that be a way out?",
        'choices': ["1. East", "2. West", "3. Search", "4. Escape"]
    },
    'antechamber': {
        'description': "With the sceptre inserted the wall begins to rumble, as you step back, loose stone and sand tumbles from the wall and with an almighty crunching sound the wall begins to part. When the newly formed opening settles into a wide doorway your jaw drops open, the glow from the immeasurably large pile of treasure fills the burial room. You are going to be the richest person alive.",
        'choices': ["1. Loot", "2. Escape"]
    }
}

"""
Entrance function to handle the first room 
"""

def entrance():
    global torch_light
    run_room = True

    light_level()
    print(room_data['entrance']['description'])

    while run_room:
        print("----------")
        for choice in room_data['entrance']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            print(torch_light)
            lower_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            print(torch_light)
            lower_left()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['entrance'].update({'choices':['1. East', '2. West', '3. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
lower_left function to handle the adventure in this room
"""

def lower_left():
    global torch_light
    run_room = True

    light_level()
    print(room_data['lower_left']['description'])

    while run_room:
        print("----------")
        for choice in room_data['lower_left']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            print(torch_light)
            middle_left()
        elif entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            print(torch_light)
            entrance()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['lower_left'].update({'choices':['1. North', '2. East', '3. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
lower_right function to handle the adventure in this room
"""

def lower_right():
    global torch_light
    run_room = True

    light_level()
    print(room_data['lower_right']['description'])

    while run_room:
        print("----------")
        for choice in room_data['lower_right']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            print(torch_light)
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            print(torch_light)
            entrance()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['lower_right'].update({'choices':['1. North', '2. West', '3. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
middle_left function to handle the adventure in this room
"""

def middle_left():
    global torch_light
    run_room = True

    light_level()
    print(room_data['middle_left']['description'])

    while run_room:
        print("----------")
        for choice in room_data['middle_left']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            print(torch_light)
            upper_left()
        elif entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            print(torch_light)
            center()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            print(torch_light)
            lower_left()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['middle_left'].update({'choices':['1. North', '2. East', '3. South', '4. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
center function to handle the adventure in this room
"""

def center():
    global torch_light
    run_room = True

    light_level()
    print(room_data['center']['description'])

    while run_room:
        print("----------")
        for choice in room_data['center']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            print(torch_light)
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            print(torch_light)
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

    light_level()
    print(room_data['middle_right']['description'])

    while run_room:
        print("----------")
        for choice in room_data['middle_right']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            print(torch_light)
            upper_right()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            print(torch_light)
            lower_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            print(torch_light)
            center()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['middle_right'].update({'choices':['1. North', '2. South', '3. West', '4. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
upper_left function to handle the adventure in this room
"""

def upper_left():
    global torch_light
    run_room = True

    light_level()
    print(room_data['upper_left']['description'])

    while run_room:
        print("----------")
        for choice in room_data['upper_left']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            burial_room()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            middle_left()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['upper_left'].update({'choices':['1. East', '2. South', '3. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
upper_right function to handle the adventure in this room
"""

def upper_right():
    global torch_light
    run_room = True

    light_level()
    print(room_data['upper_right']['description'])

    while run_room:
        print("----------")
        for choice in room_data['upper_right']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            burial_room()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['upper_right'].update({'choices':['1. South', '2. West', '3. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
burial_room function to handle the adventure in this room
"""

def burial_room():
    global torch_light
    run_room = True

    light_level()
    print(room_data['burial_room']['description'])

    while run_room:
        print("----------")
        for choice in room_data['burial_room']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            upper_left()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            upper_right()
        elif entrance_response.capitalize() == "Search":
            print("\nInvestigation Details\n")
            room_data['burial_room'].update({'choices':['1. North', '2. East', '3. West', '4. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
antechamber function to handle the adventure in this room
"""

def antechamber():
    global torch_light
    run_room = True

    light_level()
    print(room_data['antechamber']['description'])

    while run_room:
        print("----------")
        for choice in room_data['antechamber']['choices']:
            print(choice)
        print("----------")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            burial_room()
        elif entrance_response.capitalize() == "Escape":
            print("YOU WIN!")
        elif entrance_response.capitalize() == "Investigate":
            print("\nInvestigation Details\n")
            room_data['antechamber'].update({'choices':['1. South', '2. Search (Complete)']})
        else:
            print("Not a valid option, try again!\n")

"""
Light level function to check torch level as each room is entered.
"""

def light_level():
    global torch_light

    if torch_light > 3:
        print("\nBright\n")
    elif torch_light >= 1:
        print("\ndim light\n")
    else:
        game_over()
    return

"""
Game Over function to handle when the player reaches a game over scenario.
"""

def game_over():
    print("\nGAME OVER\n")



entrance()