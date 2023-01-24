from art import logo 
print(logo)
print("Welcome to guess the number")
import random

def guess_game():
    x = random.randint(0, 100)
    mode = input("Do yo want to play easy mode or hard mode?").lower()
    if mode == 'easy':
        lives = 10
    elif mode == 'hard':
        lives = 5
    else:
        return "invalid"
    should_continue = True
    while should_continue:
        guess = int(input("Guess the number: "))
        if guess == x :
            print("Yay! You win")
            should_continue = False
        elif guess > x :
            y = guess - x
            if y > 10:
                print("Too High")
            else:
                print("Slightly High")
            lives -= 1
            if lives == 0:
                should_continue = False
                print("You Lost")
        elif guess < x:
            z = x - guess
            if z > 10:
                print("Too Low")
            else:
                print("Slightly low")
            lives -= 1
            if lives == 0:
                should_continue = False
                print("You Lost")
    k = input("Do you want to play again? Type yes\n").lower()
    if k == "yes":
        guess_game()
guess_game()

    
