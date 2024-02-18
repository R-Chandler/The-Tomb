# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from clear import clear
from art import tprint
from time import sleep
"""
Global variables to be used throughout every room of the game.
"""
player = ""
weapon = ""
torch_light = 5
inventory = []
score = 0

"""
Instructions information to be called in the information screen
"""
how_to = ["\n\n Welcome intrepid explorer, you have been searching for the burial place of an ancient Pharoah for a very long time.\n Recent discoveries lead you to a remote location just outside the Valley of the Kings in Egypt.\n Your hard work has rewarded with the sight of the sealed stone doors you had always dreamed of seeing.\n You pry the doors open and walk inside...",
 "\n\nTHE TOMB is a text adventure game where your chocies will lead you to succeed in the discovery of the long lost Pharoah Raetis,\nor it can also become your tomb.",
  "As you move through the tomb, a decription of the room you are in will be displayed followed by a list of options you can do while in that area of the tomb.\n\nEnter the instruction as written to carry out that choice and progress through the tomb to find your fame and fortune.\n\n",
   "Be aware that there are hidden options leading to special rewards so do not be afraid to search for secrets.\n",
    "Be warned that your torch is also there to keep you safe, if the light goes out so do your chances of escaping the tomb.\nKeep a look out for opportunities to extend it's life as you explore.\n",
     "Your score and level of torch light wil be tracked at the top of each room, find treasures to increase your score.\n\n"
    "GOOD LUCK!\n"]





"""
Nested dictionary containing all the room descriptions, room choices and items.
"""

room_data = {
    'entrance': {
        'description': "As you cross the threshold to the tomb and move cautiously down the stone stairs you feel a stone shift under your foot making a soft click.\nSuddenly the door behind you slams shut with a loud crash. In the pitch darkness you light a torch,\nas your eyes adjust to the new gloom you see two doors leading deeper into the tomb.",
        'choices': ['1. East', '2. West', '3. Search'],
        'searched': False
    },
    'lower_left': {
        'description': "A low hiss greets you as you step through the threshold. Coiled serpent motifs adorn the walls, their eyes gleaming with a sense of knowing.\nA winding path leads deeper into the chamber, guarded by stone snake statues that seem to slither in the shadows.\nThe air is cool and filled with a faint aroma of ancient oils. In the center lies a mysterious pool reflecting the glow of a lone, suspended orb.",
        'choices': ["1. North", "2. East", "3. Search"],
        'searched': False
    },
    'lower_right': {
        'description': "As you enter the Chamber of Eternal Flames, a warm gust of air tinged with the scent of burning incense envelops you.\nTorches flicker with an ethereal flame, casting dancing shadows on the crimson walls adorned with depictions of phoenixes and fiery serpents.\nIn the center, a brazier burns with an unquenchable fire.",
        'choices': ["1. North", "2. West", "3. Search"],
        'searched': False
    },
    'middle_left': {
        'description': "In this new room a mysterious darkness cloaks the space. Dimly lit torches barely pierce the gloom, revealing walls adorned with intricate shadow play.\nThe air is thick with ancient incense. Silhouettes seem to dance along the walls as you move with the torch.\nYou get the unnerving feeling that you are being watched, a crashing sound comes from the eastern passage.",
        'choices': ["1. North", "2. East", "3. South", "4. Search"],
        'searched': False
    },
    'center': {
        'description': "You cautiously step into what seems like a crypt, the air becomes thick and oppressive. The walls are adorned with carvings of Ammit,\na monstrous amalgamation of lion, hippopotamus, and crocodile. Eerie whispers echo through the chamber, and a growl rumbles in the shadows.\nIn the center of the room lies an ancient altar, upon which rests a forbidden relic.\nAs you step towards the altar a shadowed figure slowly climbs onto it, showing you its many razor teeth in your torch light with a snarl.",
        'choices': ["1. fight", "2. Flee"],
        'flee_choices': ["1. East", "2. West"],
        'monster': "alive"
    },
    'center_clear': {
        'description': "The unmoving body of the nameless beast lays harmlessly on the floor. You now have time to marvel at the beauty of the room,\nCanpoic jars line the southern wall under a large tapestry celebrating the Pharaohs achievements in life.",
        'choices': ["1. East", "2. West", "3. Search"],
        'searched': False
    },
    'middle_right': {
        'description': "Upon entering the Chamber, an uncanny silence blankets the room.\nThe walls are adorned with faded murals portraying courtly intrigues and secrets of the ancient kingdom.\nHieroglyphic whispers seem to emerge from the very stone, telling tales of conspiracies and hidden truths.\nA central dais holds an ancient throne.\nUpon the throne sits an armour clad statue, in his outstretched hands something metal glimmers in the soft torch light.\nA muffled groan emanates from the western passageway.",
        'choices': ["1. North", "2. South", "3. West", "4. Search"],
        'searched': False
    },
    'upper_left': {
        'description': "As you step into the chamber the scent of ancient parchment fills your nostrils,\nyour torchlight flickers across the walls revealing that every inch is covered in hieroglyphs, telling tales of conquests and rituals that have long been forgotten.\nAn ominous statue stands at the north end of the room.",
        'choices': ["1. East", "2. South", "3. Search"],
        'searched': False
    },
    'upper_right': {
        'description': "Entering this grand hall you notice your footsteps are louder, echoing around the immense room.\nThe walls are lined with large statues of Anubis, the eyes of the jackal headed god seem to follow your every move.\nA pedestal standing atop a small staircase at the far end of the room catches your attention.",
        'choices': ["1. South", "2. West", "3. Search"],
        'searched': False
    },
    'burial_room': {
        'description': "This is it! You have found the room that has eluded archaeologists for centuries.\nYou find yourself standing in the burial chamber of the tomb, the walls are plastered with gold and jewels.\nGreat stone tablets stand against the eastern wall with stories carved into them depicting the great deeds of the fallen pharaoh.\nLooking to the north you see the grand sarcophagus standing in the middle of the room,\nprotection spells are engraved along the seal, they seem to glow and then you notice it… a beam of light is shining upon the lid coming from an open shaft on the ceiling…\nCould that be a way out?",
        'choices': ["1. East", "2. West", "3. Search", "4. Escape"],
        'fight_choices': ["1. Fight", "2. Flee"],
        'flee_choices': ["1. East", "2. West", "3. Escape"],
        'searched': False,
        'monster': "alive"
    },
    'antechamber': {
        'description': "With the sceptre inserted the wall begins to rumble, as you step back, loose stone and sand tumbles from the wall.\nWith an almighty crunching sound the wall begins to part. When the newly formed opening settles into a wide doorway your jaw drops open.\nThe glow from the immeasurably large pile of treasure fills the burial room.\nYou are going to be the richest person alive.",
        'choices': ["1. Loot", "2. Escape"],
        'searched': False
    }
}


def splash_screen():
    tprint("\n                               THE", font="small")
    tprint("TOMB", font="block")
    player_id()


def player_id():
    while True:
        player = input("What is your name Adventurer?:\n\n")
        player_name = player.replace(" ", "")
        if len(player_name) == 0:
            print("Please enter a name!\n")
        else:
            clear()
            print("===================")
            print(f"\nWelcome {player_name}, are you prepared to face the tomb?")
            instructions()
            break


def instructions():
    for steps in how_to:
        print(steps)
    print("PRESS ANY KEY TO CONTINUE")
    input()
    clear()
    entrance()



"""
Entrance function to handle the first room 
"""

def entrance():
    global torch_light
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['entrance']['description'])

    while run_room:
        print("====================")
        for choice in room_data['entrance']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['entrance']['searched'] == False:
                print("\nInvestigation Details\n")
                score = score + 100
                room_data['entrance'].update({'choices':['1. East', '2. West', '3. Search (Complete)']})
                room_data['entrance'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
lower_left function to handle the adventure in this room
"""

def lower_left():
    global torch_light
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['lower_left']['description'])

    while run_room:
        print("====================")
        for choice in room_data['lower_left']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_left()
        elif entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            entrance()
        elif entrance_response.capitalize() == "Search":
            if room_data['lower_left']['searched'] == False:
                print("\nInvestigation Details\n")
                score = score + 1000
                room_data['lower_left'].update({'choices':['1. North', '2. East', '3. Search (Complete)']})
                room_data['lower_left'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
lower_right function to handle the adventure in this room
"""

def lower_right():
    global torch_light
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['lower_right']['description'])

    while run_room:
        print("====================")
        for choice in room_data['lower_right']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            entrance()
        elif entrance_response.capitalize() == "Search":
            if room_data['lower_right']['searched'] == False:
                print("\nYou have found a torch!\n")
                torch_light = torch_light + 3
                score = score + 300
                room_data['lower_right'].update({'choices':['1. North', '2. West', '3. Search (Complete)']})
                room_data['lower_right'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
middle_left function to handle the adventure in this room
"""

def middle_left():
    global torch_light
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['middle_left']['description'])

    while run_room:
        print("====================")
        for choice in room_data['middle_left']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_left()
        elif entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            center()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['middle_left']['searched'] == False:
                print("\nYou have found a torch!\n")
                torch_light = torch_light + 3
                score = score + 100
                room_data['middle_left'].update({'choices':['1. North', '2. East', '3. South', '4. Search (Complete)']})
                room_data['middle_left'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
center function to handle the adventure in this room when the monster is present
"""

def center():
    global torch_light
    global score
    global weapon
    global player

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['center']['description'])

    while run_room:
        if room_data['center']['monster'] == "alive":
            print("====================")
            for choice in room_data['center']['choices']:
                print(choice)
            print("====================")
            entrance_response = input("What Do You Do Adventurer?:\n\n")
            if entrance_response.capitalize() == "Fight":
                print("\nYou stand tall facing the advancing beast, the torch light reflecting back at you in its menacing eyes")
                print("====================")
                if weapon == "Jewelled Sword":
                    print("\nMonster killed\n")
                    room_data['center'].update({'monster': "dead"})
                    score = score + 2000
                    sleep(3)
                    clear()
                    center_clear()
                else:
                    player = "dead"
                    game_over()
            elif entrance_response.capitalize() == "Flee":
                print("\nYou slowly back away from the terrifying creature as it gets ready to pounce to you sprint toward the exit!")
                print("Which way to you go?")
                print("====================")
                for choice in room_data['center']['flee_choices']:
                    print(choice)
                print("====================")
                flee_input = input("which way do you go?:\n\n")
                if flee_input.capitalize() == "East":
                    print("\nEast Chosen")
                    torch_light = torch_light -1
                    sleep(3)
                    clear()
                    middle_right()
                elif flee_input.capitalize() == "West":
                    print("West Chosen")
                    torch_light = torch_light -1
                    sleep(3)
                    clear()
                    middle_left()
                else:
                    print("Not a valid option, try again!\n")
            else:
                    print("Not a valid option, try again!\n")
        else:
            center_clear()

"""
center function to handle the adventure in this room when the monster is not present
"""


def center_clear():
    global torch_light
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['center_clear']['description'])

    while run_room:
        print("====================")
        for choice in room_data['center_clear']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['center_clear']['searched'] == False:
                print("\nInvestigation Details\n")
                score = score + 500
                room_data['center_clear'].update({'choices':['1. East', '2. West', '3. Search (Complete)']})
                room_data['center_clear'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")



"""
middle_right function to handle the adventure in this room
"""

def middle_right():
    global torch_light
    global weapon
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['middle_right']['description'])

    while run_room:
        print("====================")
        for choice in room_data['middle_right']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\nNorth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_right()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            center()
        elif entrance_response.capitalize() == "Search":
            if room_data['middle_right']['searched'] == False:
                print("\nYou have found a jewel encrusted sword, you feel safer with it in your hand.\n")
                score = score + 500
                weapon = "Jewelled Sword"
                room_data['middle_right'].update({'choices':['1. North', '2. South', '3. West', '4. Search (Complete)']})
                room_data['middle_right'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
upper_left function to handle the adventure in this room
"""

def upper_left():
    global torch_light
    global weapon
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['upper_left']['description'])

    while run_room:
        print("====================")
        for choice in room_data['upper_left']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            burial_room()
        elif entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['upper_left']['searched'] == False:
                print("\nYou have found a jewel encrusted sword, you feel safer with it in your hand.\n")
                score = score + 1000
                weapon = "Jewelled Sword"
                room_data['upper_left'].update({'choices':['1. East', '2. South', '3. Search (Complete)']})
                room_data['upper_left'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
upper_right function to handle the adventure in this room
"""

def upper_right():
    global torch_light
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['upper_right']['description'])

    while run_room:
        print("====================")
        for choice in room_data['upper_right']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "South":
            print("\nSouth Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            burial_room()
        elif entrance_response.capitalize() == "Search":
            if room_data['upper_right']['searched'] == False:
                print("\nInvestigation Details\n")
                score = score + 1000
                room_data['upper_right'].update({'choices':['1. South', '2. West', '3. Search (Complete)']})
                room_data['upper_right'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
burial_room function to handle the adventure in this room
"""

def burial_room():
    global torch_light
    global score
    global inventory
    global player
    global weapon

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['burial_room']['description'])

    while run_room:
        print("====================")
        for choice in room_data['burial_room']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\nEast Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_left()
        elif entrance_response.capitalize() == "West":
            print("\nWest Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_right()
        elif entrance_response.capitalize() == "North":
            if "golden sceptre" in inventory:
                print("You see a recess in the northern wall that looks exactly like the golden sceptre...\nyou you want to place the sceptre into the wall?\n")
                sceptre_input = input("Yes or No?\n\n")
                if sceptre_input.capitalize() == "Yes":
                    print("You place the sceptre into the hole and it fits perfectly!")
                    torch_light = torch_light -1
                    sleep(3)
                    clear()
                    antechamber()
                elif sceptre_input.capitalize() == "No":
                    print("You feel something doesn't feel right about this, you back away from the wall and turn back to the rest of the room.")
                    sleep(3)
                    clear()
                    burial_room()
                else:
                    print("Not a valid option, try again!\n")
        elif entrance_response.capitalize() == "Search":
            if room_data['burial_room']['searched'] == False:
                print("\nYou have found a torch!\n")
                score = score + 2000
                torch_light = torch_light + 3
                room_data['burial_room'].update({'choices':["1. East", "2. West", "3. North", "4. Search (Complete)", "5. Escape", "6. Open"]})
                room_data['burial_room'].update({'searched': True})
            else:
                print("You have already searched this room!")
        elif entrance_response.capitalize() == "Escape":
            print("You climb on top of the grand sarcophagus and reach for the slim opening on the ceiling,\nYou manage to squeze through the gap and feel fresh air on your face for the first time in what feels like forever!\n")
            sleep(2)
            clear()
            winner()
        elif entrance_response.capitalize() == "Open":
            if room_data['burial_room']['monster'] == "alive":
                print("\nAs you slide the heavy lid from the sarcophagus, the weight all of a sudden lessens.\n A bloodcurddling screech comes from inside the stone box and you come face to face with the undead Pharoah!")
                print("====================")
                for choice in room_data['burial_room']['fight_choices']:
                    print(choice)
                print("====================")
                entrance_response = input("What Do You Do Adventurer?:\n\n")
                if entrance_response.capitalize() == "Fight":
                    print("\nYou stand tall facing the advancing beast, the torch light reflecting back at you in its menacing eyes")
                    print("====================")
                    if weapon == "Jewelled Sword":
                        print("\nYou drive your sword into the pharoahs head, once he stops moving you notice a sceptre in his hands\n")
                        inventory.append("golden sceptre")
                        print("\nGolden Sceptre added to your inventory!\n")
                        room_data['burial_room'].update({'monster': "dead"})
                        score = score + 3000
                        sleep(3)
                        clear()
                        burial_room()
                    else:
                        player = "dead"
                        game_over()
                elif entrance_response.capitalize() == "Flee":
                    print("\nYou slowly back away from the terrifying creature as it gets ready to pounce you sprint toward the exit!")
                    print("Which way to you go?")
                    print("====================")
                    for choice in room_data['center']['flee_choices']:
                        print(choice)
                    print("====================")
                    flee_input = input("which way do you go?:\n\n")
                    if flee_input.capitalize() == "East":
                        print("\nEast Chosen")
                        torch_light = torch_light -1
                        sleep(3)
                        clear()
                        upper_right()
                    elif flee_input.capitalize() == "West":
                        print("West Chosen")
                        torch_light = torch_light -1
                        sleep(3)
                        clear()
                        upper_left()
                    elif flee_input.capitalize() == "Escape":
                        print("\nAs you step up onto the now open sarcophagus to reach the opening on the ceiling, the undead pharoah grabs your leg and pulls you into his tomb.\n\n")
                        player = "dead"
                        game_over()
                    else:
                        print("Not a valid option, try again!\n")
                else:
                    print("Not a valid option, try again!\n")
        else:
            print("Not a valid option, try again!\n")

"""
antechamber function to handle the adventure in this room
"""

def antechamber():
    global torch_light
    global score

    run_room = True

    print(f"\nScore: {score}                                   Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['antechamber']['description'])

    while run_room:
        print("====================")
        for choice in room_data['antechamber']['choices']:
            print(choice)
        print("====================")
        entrance_response = input("What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "Loot":
            if room_data['burial_room']['searched'] == False:
                print("You step towards the large pile of treasure thinking about how rich you are going to be.\nYou feel a pulling on your leg, as you look down you notice the tripwire too late as the door slams shut behind you.\n The force extinguishes your torch and you are now trapped forever with the riches you always wanted.")
                sleep(3)
                clear()
                game_over()
            else:
                print("Avoiding the tripwire, you cautiously move towards the treasure and begin looking through your new riches.")
                score = score + 10000
        elif entrance_response.capitalize() == "Escape":
            print("You climb on top of the grand sarcophagus and reach for the slim opening on the ceiling,\nYou manage to squeze through the gap and feel fresh air on your face for the first time in what feels like forever!\n")
            sleep(3)
            clear()
            winner()
        elif entrance_response.capitalize() == "Search":
            if room_data['antechamber']['searched'] == False:
                print("\nLooking around your new surroundings, between you and the treasure you notice a very fine wire stretched across the room.\n")
                room_data['antechamber'].update({'searched': True})
            else:
                print("You have already searched this room!")
        else:
            print("Not a valid option, try again!\n")

"""
Light level function to check torch level as each room is entered.
"""

def light_level():
    global torch_light

    if torch_light >= 3:
        return
    elif torch_light == 2:
        print("\nThe light of your torch is dimming, you had better find another one soon or the darkness of the tomb will take you!\n")
    elif torch_light == 1:
        print("\nYour torch is going to go out any minute! there has to be something you can use hidden around this tomb!\n")
    else:
        game_over()
    return

"""
Game Over function to handle when the player reaches a game over scenario.
"""

def game_over():
    global player
    global torch_light
    global score

    clear()
    print("\nGAME OVER\n")
    print(f"\nYour final score was: {score}\n")
    if player == "dead":
        print("\nYou were slain by a beast in the tomb!\n")
    elif torch_light == 0:
        print("\nYour torch has gone out! surrounded by darkness you succumb to the dangers of the tomb!\n")
    else:
        print("\nWhat happened?\n")
    print("\n\n Would you like to try again?\n")
    input("Press enter to play again!\n")
    clear()
    reset_game()

"""
Winner function to control what happens when the player escapes the tomb.
"""
def winner():
    global score

    print("\nCONGRATULATIONS!\n")
    print("====================")
    print(f"\nYou escaped the tomb with your life and you obtained a final score of: {score}\n")
    print("\nWish to try again?\n")
    input("Press enter to play again!\n")
    clear()
    reset_game()

"""
Reset function to return all dictionary entries and global functions to original values, then start the game again from the title screen.
"""
def reset_game():
    global player
    global weapon
    global torch_light
    global inventory
    global score

    print("\nResetting Game...\n")

    player = "alive"
    weapon = ""
    torch_light = 5
    inventory = []
    score = 0

    room_data['entrance'].update({'choices':['1. East', '2. West', '3. Search']})
    room_data['lower_left'].update({'choices':["1. North", "2. East", "3. Search"]})
    room_data['lower_right'].update({'choices':["1. North", "2. West", "3. Search"]})
    room_data['middle_left'].update({'choices':["1. North", "2. East", "3. South", "4. Search"]})
    room_data['center_clear'].update({'choices':["1. East", "2. West", "3. Search"]})
    room_data['middle_right'].update({'choices':["1. North", "2. South", "3. West", "4. Search"]})
    room_data['upper_left'].update({'choices':["1. East", "2. South", "3. Search"]})
    room_data['upper_right'].update({'choices':["1. South", "2. West", "3. Search"]})
    room_data['burial_room'].update({'choices':["1. East", "2. West", "3. Search", "4. Escape"]})
    room_data['antechamber'].update({'choices':["1. Loot", "2. Escape"]})

    room_data['entrance'].update({'searched': False})
    room_data['lower_left'].update({'searched': False})
    room_data['lower_right'].update({'searched': False})
    room_data['middle_left'].update({'searched': False})
    room_data['center_clear'].update({'searched': False})
    room_data['middle_right'].update({'searched': False})
    room_data['upper_left'].update({'searched': False})
    room_data['upper_right'].update({'searched': False})
    room_data['burial_room'].update({'searched': False})
    room_data['antechamber'].update({'searched': False})

    room_data['center'].update({'monster': "alive"})
    room_data['burial_room'].update({'monster': "alive"})

    sleep(2)
    print("\nGame Successfully Reset... Returning to title screen...\n")
    sleep(2)
    clear()
    main()

"""
Defining main function to control the game
"""
def main():
    splash_screen()


"""
Call main function to begin the game
"""
main()