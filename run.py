from clear import clear
from art import tprint
from time import sleep
"""
Global variables to be used throughout every room of the game.
"""
player_name = ""
player = ""
weapon = ""
torch_light = 5
inventory = []
high_score = 0
score = 0

"""
Instructions information to be called in the information screen
"""
page_one = ["\n\n Welcome intrepid explorer, you have been searching for the burial place of\n an ancient Pharoah for a very long time. Recent discoveries lead you to a\n remote location just outside the Valley of the Kings in Egypt.\n Your hard work has rewarded with the sight of the sealed doors\n you had always dreamed of seeing. You pry the doors open and walk inside...",
 "\n\n THE TOMB is a text adventure game where your chocies will lead you to succeed\n in the discovery of the long lost Pharoah Raetis,\n or it can also become your tomb.\n\n",
  " As you move through the tomb, a decription of the rooms will be displayed\n followed by a list of options you can do while in that area of the tomb.\n\n Enter the instruction as written (eg. 'East/east') to carry out that choice\n and progress through the tomb to find your fame and fortune.\n\n"]

page_two = ["\n\n Be aware that there are hidden options leading to special rewards\n so do not be afraid to search for secrets.\n",
" Be warned that your torch is also there to keep you safe,\n if the light goes out so do your chances of escaping the tomb.\n Keep a look out for opportunities to extend it's life as you explore.\n",
 " Your score and level of torch light wil be tracked at the top of each room,\n find treasures to increase your score.\n\n",
  "   GOOD LUCK!\n"]


"""
Nested dictionary containing all the room descriptions, room choices and items.
"""

room_data = {
    'entrance': {
        'description': " As you cross the threshold to the tomb and move cautiously down the stone\n stairs you feel a stone shift under your foot making a soft click.\n Suddenly the door behind you slams shut with a loud crash.\n In the pitch darkness you light a torch, as your eyes adjust to the new gloom\n you see two doors leading deeper into the tomb.",
        'choices': [' 1. East', ' 2. West', ' 3. Search'],
        'searched': False,
        'search_notes': " You inspect the doors and find no possible way of getting them open.\n While searching the rest of the room you find little of note."
    },
    'lower_left': {
        'description': " A low hiss greets you as you step through the threshold. Coiled serpent motifs\n adorn the walls, their eyes gleaming with a sense of knowing.\n A winding path leads deeper into the chamber, guarded by stone snake statues\n that seem to slither in the shadows. The air is cool and filled with a faint\n aroma of ancient oils. In the center lies a mysterious pool reflecting the\n glow of a lone, suspended orb.",
        'choices': [" 1. North", " 2. East", " 3. Search"],
        'searched': False,
        'search_notes': " You step up to the suspended orb and reach out to touch it. without warning\n the orb explodes with a blinding light forcing you to close your eyes.\n When you open them again you notice that the mouth of one of the snake statues\n has opened revealing a beautiful pendant."
    },
    'lower_right': {
        'description': " As you enter the Chamber of Eternal Flames, a warm gust of air tinged with\n the scent of burning incense envelops you. Torches flicker with an ethereal\n flame, casting dancing shadows on the crimson walls adorned with depictions\n of phoenixes and fiery serpents. In the center,\n a brazier burns with an unquenchable fire.",
        'choices': [" 1. North", " 2. West", " 3. Search"],
        'searched': False,
        'search_notes': " Glancing around and taking in the image of each mural you notice that to\n the side of one large phoenix an unlit torch sits in an alcove on the wall.\n You remove the torch and place it in your bag, just in case."
    },
    'middle_left': {
        'description': " In this new room a mysterious darkness cloaks the space. Dimly lit torches\n barely pierce the gloom, revealing walls adorned with intricate shadow play.\n The air is thick with ancient incense. Silhouettes seem to dance along the\n walls as you move with the torch. You get the unnerving feeling that you are\n being watched, a crashing sound comes from the eastern passage.",
        'choices': [" 1. North", " 2. East", " 3. South", " 4. Search"],
        'searched': False,
        'search_notes': " In the center of the room stands a magnificent candelabra,\n fortune favours you as one torch has remained untouched.\n You remove the fresh torch and place it in your bag."
    },
    'center': {
        'description': " You cautiously step into what seems like a crypt, the air becomes thick\n and oppressive. The walls are adorned with carvings of Ammit,\n a monstrous amalgamation of lion, hippopotamus, and crocodile. Eerie whispers\n echo through the chamber, and a growl rumbles in the shadows.\n In the center of the room lies an ancient altar, upon which rests a forbidden\n relic. As you step towards the altar a shadowed figure slowly climbs onto it,\n showing you its many razor teeth in your torch light with a snarl.",
        'choices': [" 1. fight", " 2. Flee"],
        'flee_choices': [" 1. East", " 2. West"],
        'monster': "alive"
    },
    'center_clear': {
        'description': " The unmoving body of the nameless beast lays harmlessly on the floor.\n You now have time to marvel at the beauty of the room,\n Canpoic jars line the southern wall under a large tapestry celebrating the\n Pharaohs achievements in life.",
        'choices': [" 1. East", " 2. West", " 3. Search"],
        'searched': False,
        'search_notes': " Reading the texts written across the altar you learn that this is the final\n resting place of the Pharaohs most trusted advisor.\n The relic is a large golen eye which seems to follow you around the room.\n You place the relic into your bag."
    },
    'middle_right': {
        'description': " Upon entering the Chamber, an uncanny silence blankets the room.\n The walls are adorned with faded murals portraying courtly intrigues and\n secrets of the ancient kingdom. Hieroglyphic whispers seem to emerge from the\n very stone, telling tales of conspiracies and hidden truths.\n A central dais holds an ancient throne. Upon the throne sits an armour clad\n statue, in his hands something metal glimmers in the soft torch light.\n A muffled groan emanates from the western passageway.",
        'choices': [" 1. North", " 2. South", " 3. West", " 4. Search"],
        'searched': False,
        'search_notes': " You step towards the statue and it immediately becomes clear that this\n is a statue of the Pharaohs trusted general. In his hands he is holding\n a beautiful jewel encrusted blade, likely a ceremonial blade\n but you feel safer holding it in your own hands."
    },
    'upper_left': {
        'description': " As you step into the chamber the scent of ancient parchment\n fills your nostrils, your torchlight flickers across the walls revealing that\n every inch is covered in hieroglyphs, telling tales of conquests and rituals\n that have long been forgotten. An ominous statue stands at the north end of the room.",
        'choices': [" 1. East", " 2. South", " 3. Search"],
        'searched': False,
        'search_notes': " Sifting through the endless scrolls you find a near completely\n documented history of Pharoah Raetis' reign.\n This would be priceless if given to the right people."
    },
    'upper_right': {
        'description': " Entering this grand hall you notice your footsteps are louder, echoing around\n the immense room. The walls are lined with large statues of Anubis,\n the eyes of the jackal headed god seem to follow your every move.\n A pedestal standing atop a small staircase at the far end of the room catches\n your attention.",
        'choices': [" 1. South", " 2. West", " 3. Search"],
        'searched': False,
        'search_notes': " You make your way towards the pedestal, as you get closer you realise\n that this is a pile of offerings left by the people when the Pharoah passed.\n There are hundreds of precious stones and gems,\n you fill your pockets and press on."
    },
    'burial_room': {
        'description': " This is it!\n You have found the room that has eluded archaeologists for centuries.\n You find yourself standing in the burial chamber of the tomb,\n the walls are plastered with gold and jewels. Great stone tablets stand\n against the eastern wall with stories carved into them depicting the\n great deeds of the fallen pharaoh.\n Looking to the north you see the grand sarcophagus standing\n in the middle of the room, protection spells are engraved along the seal,\n they seem to glow and then you notice it… a beam of light is shining\n upon the lid coming from an open shaft on the ceiling…\n Could that be a way out?",
        'choices': [" 1. East", " 2. West", " 3. Search", " 4. Escape"],
        'fight_choices': [" 1. Fight", " 2. Flee"],
        'flee_choices': [" 1. East", " 2. West", " 3. Escape"],
        'searched': False,
        'monster': "alive",
        'search_notes': " At the foot of the sarcophagus stands a fresh torch which you add to your bag.\n With further investigation you realise that the lid of the tomb\n is slightly ajar and you could open it to see whats inside.\n Something from the northern wall also catches your attention."
    },
    'antechamber': {
        'description': " With the sceptre inserted the wall begins to rumble, as you step back, loose\n stone and sand tumbles from the wall. With an almighty crunching sound\n the wall begins to part. When the newly formed opening settles into a wide\n doorway your jaw drops open. The glow from the immeasurably large pile\n of treasure fills the burial room.\nYou are going to be the richest person alive.",
        'choices': [" 1. Loot", " 2. Escape"],
        'searched': False,
        'search_notes': " Looking around your new surroundings, between you and the mountain of treasure\n you notice a very fine wire stretched across the room.\n you recognise this to be trap designed to protect the Pharoah's riches."
    }
}


def splash_screen():
    tprint("\n                               THE", font="small")
    tprint("TOMB", font="block")
    player_id()


def player_id():
    global player_name

    while True:
        player = input(" What is your name Adventurer?:\n\n")
        player_name = player.replace(" ", "")
        if len(player_name) == 0:
            print(" Please enter a name!\n")
        else:
            clear()
            instructions()
            


def instructions():
    global player_name

    print(" ===================")
    print(f" Welcome {player_name}, are you prepared to face the tomb?")
    for x in page_one:
        print(x)
    input(" PRESS ENTER TO CONTINUE\n")
    clear()
    for y in page_two:
        print(y)
    input(" PRESS ENTER TO CONTINUE\n")
    clear()
    entrance()



"""
Entrance function to handle the first room 
"""

def entrance():
    global torch_light
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['entrance']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['entrance']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\n East Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_right()
        elif entrance_response.capitalize() == "West":
            print("\n West Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['entrance']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['entrance']['search_notes'])
                score = score + 100
                room_data['entrance'].update({'choices':[' 1. East', ' 2. West', ' 3. Search (Complete)']})
                room_data['entrance'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
lower_left function to handle the adventure in this room
"""

def lower_left():
    global torch_light
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['lower_left']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['lower_left']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\n North Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_left()
        elif entrance_response.capitalize() == "East":
            print("\n East Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            entrance()
        elif entrance_response.capitalize() == "Search":
            if room_data['lower_left']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['lower_left']['search_notes'])
                score = score + 1000
                room_data['lower_left'].update({'choices':[' 1. North', ' 2. East', ' 3. Search (Complete)']})
                room_data['lower_left'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
lower_right function to handle the adventure in this room
"""

def lower_right():
    global torch_light
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['lower_right']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['lower_right']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\n North Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\n West Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            entrance()
        elif entrance_response.capitalize() == "Search":
            if room_data['lower_right']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['lower_right']['search_notes'])
                torch_light = torch_light + 3
                score = score + 300
                room_data['lower_right'].update({'choices':[' 1. North', ' 2. West', ' 3. Search (Complete)']})
                room_data['lower_right'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
middle_left function to handle the adventure in this room
"""

def middle_left():
    global torch_light
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['middle_left']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['middle_left']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\n North Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_left()
        elif entrance_response.capitalize() == "East":
            print("\n East Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            center()
        elif entrance_response.capitalize() == "South":
            print("\n South Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['middle_left']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['middle_left']['search_notes'])
                torch_light = torch_light + 3
                score = score + 100
                room_data['middle_left'].update({'choices':[' 1. North', ' 2. East', ' 3. South', ' 4. Search (Complete)']})
                room_data['middle_left'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
center function to handle the adventure in this room when the monster is present
"""

def center():
    global torch_light
    global high_score
    global score
    global weapon
    global player

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['center']['description'])

    while run_room:
        if room_data['center']['monster'] == "alive":
            print(" ====================")
            for choice in room_data['center']['choices']:
                print(choice)
            print(" ====================")
            entrance_response = input(" What Do You Do Adventurer?:\n\n")
            if entrance_response.capitalize() == "Fight":
                print("\n You stand tall facing the advancing beast,\n the torch light reflecting back at you in its menacing eyes")
                print(" ====================")
                if weapon == "Jewelled Sword":
                    print("\n Monster killed\n")
                    room_data['center'].update({'monster': "dead"})
                    score = score + 2000
                    sleep(3)
                    clear()
                    center_clear()
                else:
                    player = "dead"
                    game_over()
            elif entrance_response.capitalize() == "Flee":
                print("\n You slowly back away from the terrifying creature as it gets ready to pounce,\n you sprint toward the exit!")
                print(" Which way to you go?")
                print(" ====================")
                for choice in room_data['center']['flee_choices']:
                    print(choice)
                print(" ====================")
                flee_input = input(" which way do you go?:\n\n")
                if flee_input.capitalize() == "East":
                    print("\n East Chosen")
                    torch_light = torch_light -1
                    sleep(3)
                    clear()
                    middle_right()
                elif flee_input.capitalize() == "West":
                    print(" West Chosen")
                    torch_light = torch_light -1
                    sleep(3)
                    clear()
                    middle_left()
                else:
                    print(" Not a valid option, try again!\n")
            else:
                print(" Not a valid option, try again!\n")
        else:
            center_clear()

"""
center function to handle the adventure in this room when the monster is not present
"""


def center_clear():
    global torch_light
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['center_clear']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['center_clear']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\n East Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\n West Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['center_clear']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['center_clear']['search_notes'])
                score = score + 500
                room_data['center_clear'].update({'choices':[' 1. East', ' 2. West', ' 3. Search (Complete)']})
                room_data['center_clear'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")



"""
middle_right function to handle the adventure in this room
"""

def middle_right():
    global torch_light
    global weapon
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['middle_right']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['middle_right']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "North":
            print("\n North Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_right()
        elif entrance_response.capitalize() == "South":
            print("\n South Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            lower_right()
        elif entrance_response.capitalize() == "West":
            print("\n West Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            center()
        elif entrance_response.capitalize() == "Search":
            if room_data['middle_right']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['middle_right']['search_notes'])
                score = score + 500
                weapon = "Jewelled Sword"
                room_data['middle_right'].update({'choices':[' 1. North', ' 2. South', ' 3. West', ' 4. Search (Complete)']})
                room_data['middle_right'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
upper_left function to handle the adventure in this room
"""

def upper_left():
    global torch_light
    global weapon
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['upper_left']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['upper_left']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\n East Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            burial_room()
        elif entrance_response.capitalize() == "South":
            print("\n South Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_left()
        elif entrance_response.capitalize() == "Search":
            if room_data['upper_left']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['upper_left']['search_notes'])
                score = score + 1000
                weapon = "Jewelled Sword"
                room_data['upper_left'].update({'choices':[' 1. East', ' 2. South', ' 3. Search (Complete)']})
                room_data['upper_left'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
upper_right function to handle the adventure in this room
"""

def upper_right():
    global torch_light
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['upper_right']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['upper_right']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "South":
            print("\n South Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            middle_right()
        elif entrance_response.capitalize() == "West":
            print("\n West Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            burial_room()
        elif entrance_response.capitalize() == "Search":
            if room_data['upper_right']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['upper_right']['search_notes'])
                score = score + 1000
                room_data['upper_right'].update({'choices':[' 1. South', ' 2. West', ' 3. Search (Complete)']})
                room_data['upper_right'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
burial_room function to handle the adventure in this room
"""

def burial_room():
    global torch_light
    global high_score
    global score
    global inventory
    global player
    global weapon

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['burial_room']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['burial_room']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "East":
            print("\n East Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_right()
        elif entrance_response.capitalize() == "West":
            print("\n West Chosen")
            torch_light = torch_light -1
            sleep(3)
            clear()
            upper_left()
        elif entrance_response.capitalize() == "North":
            if "golden sceptre" in inventory:
                print("\n You see a recess in the northern wall that looks like the golden sceptre...\n do you want to place the sceptre into the wall?\n")
                sceptre_input = input(" Yes or No?\n\n")
                if sceptre_input.capitalize() == "Yes":
                    print("\n You place the sceptre into the hole and it fits perfectly!")
                    torch_light = torch_light -1
                    sleep(3)
                    clear()
                    antechamber()
                elif sceptre_input.capitalize() == "No":
                    print("\n You feel something doesn't feel right about this,\n you back away from the wall and turn back to the rest of the room.")
                    sleep(3)
                    clear()
                    burial_room()
                else:
                    print(" Not a valid option, try again!\n")
            else:
                print(" You investigate the northern wall and find nothing but\n a suspicous recess in the wall that looks like a sceptre.")
        elif entrance_response.capitalize() == "Search":
            if room_data['burial_room']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['burial_room']['search_notes'])
                score = score + 2000
                torch_light = torch_light + 3
                room_data['burial_room'].update({'choices':[" 1. East", " 2. West", " 3. North", " 4. Search (Complete)", " 5. Escape", " 6. Open"]})
                room_data['burial_room'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        elif entrance_response.capitalize() == "Escape":
            print(" You climb on top of the grand sarcophagus and reach for the\n slim opening on the ceiling, You manage to squeze through the gap and feel\n fresh air on your face for the first time in what feels like forever!\n")
            sleep(3)
            clear()
            winner()
        elif entrance_response.capitalize() == "Open":
            if room_data['burial_room']['monster'] == "alive":
                print("\n As you slide the heavy lid from the sarcophagus, the weight all of a sudden\n lessens. A bloodcurddling screech comes from inside the stone box and you\n come face to face with the undead Pharoah!")
                print(" ====================")
                for choice in room_data['burial_room']['fight_choices']:
                    print(choice)
                print(" ====================")
                entrance_response = input(" What Do You Do Adventurer?:\n\n")
                if entrance_response.capitalize() == "Fight":
                    print("\n You stand tall facing the advancing beast,\n the torch light reflecting back at you in its menacing eyes\n")
                    sleep(3)
                    clear()
                    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                    if weapon == "Jewelled Sword":
                        print("\n You drive your sword into the pharoahs head,\n once he stops moving you notice a sceptre in his hands\n")
                        inventory.append("golden sceptre")
                        print("\n Golden Sceptre added to your inventory!\n")
                        room_data['burial_room'].update({'monster': "dead"})
                        score = score + 3000
                        sleep(3)
                        clear()
                        burial_room()
                    else:
                        player = "dead"
                        clear()
                        game_over()
                elif entrance_response.capitalize() == "Flee":
                    print("\n You slowly back away from the terrifying creature as it gets ready to pounce,\n you sprint toward the exit!")
                    print(" ====================")
                    for choice in room_data['center']['flee_choices']:
                        print(choice)
                    print(" ====================")
                    flee_input = input(" which way do you go?:\n\n")
                    if flee_input.capitalize() == "East":
                        print("\n East Chosen")
                        torch_light = torch_light -1
                        sleep(3)
                        clear()
                        upper_right()
                    elif flee_input.capitalize() == "West":
                        print(" West Chosen")
                        torch_light = torch_light -1
                        sleep(3)
                        clear()
                        upper_left()
                    elif flee_input.capitalize() == "Escape":
                        print("\n As you step up onto the now open sarcophagus\n to reach the opening on the ceiling, the undead pharoah\n grabs your leg and pulls you into his tomb.\n\n")
                        player = "dead"
                        clear()
                        game_over()
                    else:
                        print(" Not a valid option, try again!\n")
                else:
                    print(" Not a valid option, try again!\n")
        else:
            print(" Not a valid option, try again!\n")

"""
antechamber function to handle the adventure in this room
"""

def antechamber():
    global torch_light
    global high_score
    global score

    run_room = True

    clear()
    print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
    light_level()
    print(room_data['antechamber']['description'])

    while run_room:
        print(" ====================")
        for choice in room_data['antechamber']['choices']:
            print(choice)
        print(" ====================")
        entrance_response = input(" What Do You Do Adventurer?:\n\n")
        if entrance_response.capitalize() == "Loot":
            if room_data['burial_room']['searched'] == False:
                clear()
                print(" You step towards the large pile of treasure thinking about how rich you are going to be.\n You feel a pulling on your leg, as you look down you notice the tripwire too late as the door slams shut behind you.\n The force extinguishes your torch and you are now trapped forever with the riches you always wanted.")
                sleep(3)
                clear()
                game_over()
            else:
                print(" Avoiding the tripwire, you cautiously move towards the treasure\n and begin looking through your new riches.")
                score = score + 10000
        elif entrance_response.capitalize() == "Escape":
            print(" You climb on top of the grand sarcophagus and reach for the\n slim opening on the ceiling, You manage to squeze through the gap and feel\n fresh air on your face for the first time in what feels like forever!\n")
            sleep(3)
            clear()
            winner()
        elif entrance_response.capitalize() == "Search":
            if room_data['antechamber']['searched'] == False:
                clear()
                print(f" Score: {score}           High Score:{high_score}             Torch Level: {torch_light}\n\n")
                print(room_data['antechamber']['search_notes'])
                room_data['antechamber'].update({'searched': True})
                sleep(3)
            else:
                print(" You have already searched this room!")
        else:
            print(" Not a valid option, try again!\n")

"""
Light level function to check torch level as each room is entered.
"""

def light_level():
    global torch_light

    if torch_light >= 3:
        return
    elif torch_light == 2:
        print("\n The light of your torch is dimming, you had better find another one soon\n or the darkness of the tomb will take you!\n")
    elif torch_light == 1:
        print("\n Your torch is going to go out any minute! there has to be something\n you can use hidden around this tomb!\n")
    else:
        game_over()
    return


"""
high_score function wil read the score and compare it to the current high score, if the score is higher it will replace the high score for further attempts.
"""
def new_high_score():
    global high_score
    global score

    if score > high_score:
        print(f"\n Well done you've achieved a new high score of {score}!")
        print(" ====================")
        high_score = score
    else:
        print("\n You didn't beat your high score this time.")
        print(" ====================")


"""
Game Over function to handle when the player reaches a game over scenario.
"""

def game_over():
    global player_name
    global player
    global torch_light
    global score

    clear()
    print("\n GAME OVER\n")
    print(f"\n {player_name} Your final score was: {score}\n")
    if player == "dead":
        print(f"\n You were slain by a beast in the tomb!\n")
    elif torch_light == 0:
        print(f"\n Your torch has gone out!\n\n surrounded by darkness you succumb to the dangers of the tomb!\n")
    else:
        print("\n What happened?\n")

    print(" ====================")
    new_high_score()
    print("\n\n Would you like to try again?\n")
    input(" Press enter to play again!\n")
    clear()
    reset_game()


"""
Winner function to control what happens when the player escapes the tomb.
"""
def winner():
    global player_name
    global score

    print(f"\n CONGRATULATIONS {player_name}!\n")
    print(" ====================")
    new_high_score()
    print(f"\n You escaped the tomb with your life and you obtained a final score of: {score}\n")
    print("\n Wish to try again?\n")
    input(" Press enter to play again!\n")
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

    print("\n Resetting Game...\n")

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
    print("\n Game Successfully Reset... Returning to title screen...\n")
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