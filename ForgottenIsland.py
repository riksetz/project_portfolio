# Forgotten Island. Day 3 Project. Date: Friday, 08/09/2023.

import math

while True:
    programname = "Forgotten Island"
    print (f"\nWelcome to {programname}.\n")
    player = input("Enter player's name: ")
    print (f"\nHi {player}, you are stranded on a forgotten island. To return home you must find the hidden treasure without dying.\nGoodluck!\n")

    ready = input("Ready to start? (Y/N)\n").lower()
    while ready != "y":
        ready = input("Ready to start? (Y/N)\n").lower()
    print ('''
                                ,@@@@@@@,
                        ,,,.   ,@@@@@@/@@,  .oo8888o.          
        LEFT  <---   ,&%%&%&&%,@@@@@/@@@ @@@,8888\88/8o    RIGHT --->    
                    ,%&\%&&%&&%,@@@\@@@/@@@ 88\88888/88'
                    %&&%&%&/%&&%@@\@@/ /@@@ 88888\88888'
                    %&&%/ %&%%&&@@\ V /@@'  `88\8 `/88'
                    `&%\ ` /%&'    |.|        \ '|8'
                        |o|        | |         | |
                        |.|        | |         | |
                    \\  / ._\//_/__/  ,\_//__\\/.  \_//__/_
    ''')
    turn = input("You encounter two paths.\nTurn left or right (L/R): ").lower()
    while turn != "l" and turn != "r":
        turn = input("Invalid response. Enter: (L/R)\n").lower()
    if turn == "l":
        print(''' 
                              /| o
                             /_|=/
                            /__|<|
        ~-~-~-~-~-~-~-~-~-~-~======~-~-~-~
         ~~~        ~~~     ` _)('
               ~~~           ` )=`
                              `' *
        ''')
        print(f"{player} you have reached a river, you must get across to the other side.\nYou see the tip of a boat sail in the distance but it is moving further away. Quick!\n")
        river = input("Select Option:\n1. Swim towards the boat.\n2. Create smoke and wait for boat to come towards you.\n3. Scream HELPPPP!\n")
        while river != "1" and river != "2" and river != "3":
            river = input("Invalid response. Enter (1, 2 or 3): ").lower()
        if river == "2":
            print("\nThe sailor sees your smoke and the boat approaches you, you are saved! (sike)\n")
            print ('''
                   _~
                _~ )_)_~
                )_))_))_)
                _!__!__!_
                \_______/
            ~~~~~~~~~~~~~~~~~
            ''')
            print(f"Sailor: Nice to meet you {player}, my name is Jack.\nI need your help to find the treasure chest on the island.\n")
            print("There is a map inside the chest, without it we can't find shore.")
            print ('''
                   _..._    _..._
              _..-"      `Y`      "-._
              \     N    |           /
              \\  W  +  E | compass  //
              \\\    S    |         ///
               \\\ _..---.|.---.._ ///
                \\`_..---.Y.---.._`//
                 '`               `'
            ''')
            compass = input("Your compass broke. Now trusting your life in a dusty ass book you devide to turn the boat ->\nNorth(N), East(E), South(S), West(W): ").lower()
            while compass != "n" and compass != "e" and compass != "s" and compass!= "w":
                compass = input("Invalid response. Enter (N, E ,S or W): ").lower()
            if compass == "n" or compass == "s":
                print (f"\nCongratualtions, WINNER! {player} and their sailor friend Jack find the treasure chest and return home safely.\n")
                print (f'''
                *******************************************************************************
                         |                   |                  |                     |
                _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|__________________
                        |                `"=._o`"=._        _`"=._                    |
                _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                         |            |o`"=._` , "` `; .". ,  "-._"-._; ;'             |
                _________|___________ | ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._ {player}      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/_____/__
                ******************************************************************************* 
                ''')
            else:
                print("\nYou get caught in a windstorm and die.\n       GAME OVER.")
        elif river == "1":
            print ('''
                            _.---._     .---.
                    __...---' .---. `---'-.   `.
                .-''__.--' _.'( | )`.  `.  `._ :
            .'__-'_ .--'' ._`---'_.-.  `.   `-`.
                    ~ -._ -._``---. -.    `-._   `.
                        ~ -.._ _ _ _ ..-_ `.  `-._``--.._
                                    -~ -._  `-.  -. `-._``--.._.--''.
                                            ~ ~-.__     -._  `-.__   `. `.
                                                ~~ ~---...__ _    ._ .` `.
                                                            ~  ~--.....--~`
            ''')
            print(f"{player} died from becoming crocodile lunch.\n       GAME OVER.")
        else:
            print (f"{player} dies from starvation.\n       GAME OVER.")
    else:
        print (f"{player} died from walking into a poisonous bush.\n        GAME OVER.")
    restart = input(f"\nPlay {programname} again: (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n") 
        break
    print(f"Restarting {programname}...\n")
