# This program is a random number guessing game
# 11/5/2019
# CTI-110 P5HW1 - Random Number
# Francesco Archino

def main():
    mainMenu()



def mainMenu():
    mainMenu
    print("I-------------------------------------I\n")
    print("\t Main Menu\n")
    print("\t 1) Play Game \n")
    print("\t 2) Exit\n")
    print("I-------------------------------------I\n")


import random

hidden = random.randrange(1, 100)

 
guess = int(input("Please enter your guess: "))
 
if guess == hidden:
    print("Hit!", hidden)
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")


main()
    
