import random
print("Welcome to the coin toss emulator")
x = input("Do you want to toss the coin? Y \n")
x = x.lower()
if x == 'y':
    z = random.randint(0,1)
    if z == 0:
        print("Heads")
    else:
        print("Tails")
else:
    print("please enter correct option")