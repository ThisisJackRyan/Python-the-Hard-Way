from sys import exit

def gold_room():
    print("this room is full of gold. how muyuch do you take")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much  =int(choice)
    else:
        dead("Man, learn to type a number")
    if how_much < 50:
        print("Nice, you're not greed, you win!")
        exit(0)
    else:
        dead("You greedy boi")
    

def bear_room():
    print("there is a bear here .")
    print("the bear has a bunch of honey")
    print("The fat bear is in front of another door. ")
    print("How are you going to moe the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door.")
            print("you can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear in fact chewed your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")
            
        

def cthulhu_room():
    print("here you see the great evil Cthulhu. ")
    print("he, it , whatever stares at yu and you go insane")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was Tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around till you starve.")


start()