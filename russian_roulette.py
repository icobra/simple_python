#!/usr/bin/python3
# Russian roulette with seven-shot revolver.
from random import randint

def guess():
    # Check user input and return correct answer
    while True:
        number = input("Press '1' ,'2' or 'e(xit)'  and then press 'Enter'")
        if number == '1' or number == '2':
            return number
        elif number == 'e':
            exit()
        else:
            print("Incoret input")

def roulette():
    # Spin chamber and pull trigger.
    life = None # True for live, and false for dead
    if (randint(0,100)) > 30:   # Condition to successful validation pull trigger.
        life = True
    else:
        life = False
    return life

def game():
    # main loop of game
    pressure_counter = 0
    while pressure_counter < 7:
        chose = guess()
        if chose == '1':
            life = roulette()
            # Check life
            if life:
                print("-CLICK-")
                pressure_counter += 1
            else:
                print("BANG! YOU ARE DEAD!!!")
                return
        else:
            print("Ha ha ha. Chicken!!!")
            return
    if pressure_counter == 7:
        print("YOU WIN!!!")

def main():
    game_status = True
    while game_status:
        print("""
Russian roulette. \n
This a game of >>>>>>> RUSSIAN ROULETTE. \n
DO NOT TRY THIS IN REALITY!!!\n
Here is a seven-shot revolver.
Type '1' to spin chamber and pull trigger.
Type '2' to give up.
Go... """)
        game()
        print(""" \n\n\n
Do you want play again?
Type '1' or '2' to yes and 'e' to exit""")
        game_status = guess()
        print(" \n\n\n")
    print("Bye, bye. Thank you to playing.")

if __name__ == "__main__":
    main()
