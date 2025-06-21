

# MINI PROJECTS - 01 : -

#) Game Name : GUESS THE NUMBER -

# Description : Our Program will automatically generate a random number in between our given range, lets say that generated number is our traget to GUESS.Now, We need to write the program to guess the generated number untill we dont GUESS the correct number, till then we take input from user(with optional Quit Functionality to Quit the game in between).If entered number is less than generted number we will show a prompt to enter the bigger number and if entered number is bigger than generated number, we will show a prompt to enter smaller number.

import random

randGeneratedNo = random.randint(1, 100) # 1 and 100 Included In the Range.

while True:

    choiceValue = input("Enter the Guess Number or Quit(type 'Quit') :")
    
    if(choiceValue == "Quit"):
        print("Thanks For Playing The Game,Try Again In Spare Time..!")
        break
    
    choiceValue = int(choiceValue)
    if(choiceValue == randGeneratedNo):
        print("Success : CORRECT GUESS!!")
        break
    elif(choiceValue < randGeneratedNo):
        print("Your entered number was too small, take a Bigger Guess Value...")
    else:
        print("Your entered number was too big, take a smaller Guess Value...")

print("--------GAME OVER--------")