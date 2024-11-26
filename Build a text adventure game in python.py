def start_game():
    print("Welcome to the SASSY's adventure game!")
    print("You are standing at the entrance of a CAVE!!")
    print("There are two paths to choose from.")
    print("Do you want to go 'north' or 'south'?")
    choice = input("> ")
    if choice.lower() == "north":
        bear_room()
    elif choice.lower() == "south":
        cthulhu_room()
    else:
        dead("You stumble around the cave until you starve.")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear? enter 'take honey' or 'taunt bear'")
    choice = input("> ")
    if choice.lower() == "take honey":
        dead("The bear looks at you then slaps your face off.")
    elif choice.lower() == "taunt bear" or choice.lower() == "taunt" or choice.lower() == "yeild":
        gold_room()
    else:
        bear_room()

def gold_room():
    print("This room is full of gold. How much do you take? (enter only '0' to '100' how much you need)")
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def cthulhu_room():
    print("Here you see the great evil/savior SASETHAR !! ")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you want 're-life' for your life or eat your 'head'?")
    choice = input("> ")
    if "re-life" in choice.lower():
        start_game()
    elif "head" in choice.lower():
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why)
    print("Game Over")

start_game()