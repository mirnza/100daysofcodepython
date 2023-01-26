import random

from game_data import data

from art import logo
from art import vs

import os
def assign():
    return random.choice(data)

def compare(p1, p2, user_input):
    sum1 = p1['follower_count']
    sum2 = p2['follower_count']

    max = ""
    if sum1 > sum2:
        max = p1['name']
    elif sum2 > sum1:
        max = p2['name']
    
    if max == user_input:
        return True
    else:
        return False
    

def play_higher_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing = True
        while still_guessing:
            os.system('clear')
            print(logo)

            person1 = assign()
            person2 = assign()

            if score > 0:
                person1 = person2
                person2 = assign()

            print(f"Name: {person1['name']}, Description: {person1['description']}")
            print(vs)
            print(f"Name: {person2['name']}, Description: {person2['description']}")

            print("----------------------------------------")
            print(f"Your current score is {score}")
            print("----------------------------------------")

            guess = input("Enter The name of highest follower:   ")

            if compare(person1, person2, guess):
                score += 1
            else:
                still_guessing = False

        play_again = input("Do you want to play again(y/n):  ").lower()
        if play_again == 'y':
            continue
        elif play_again == 'n':
            playing_game = False
            os.system('clear')
            print("Game exited succesfully")
        else:
            playing_game = False
            os.system('clear')
            print('Invalid input taken as a N, Game exited')
            


want_to_play = input("do you want to play higher or lower? (y/n)").lower()
if want_to_play == "y":
    os.system('clear')
    play_higher_lower()
elif want_to_play == "n":
    print("Program exit succesfull")
else:
    print("Invalid output. Program quits!!!!!!!!")

