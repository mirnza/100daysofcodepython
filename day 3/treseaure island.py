print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_________
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
turn = input("Where do yo wanna go? Left or Right\n")
t = turn.lower()

if t == ('left'):
    print("You are now on the shore of ocean")
    step2 = input("what do you want to do wait for the boat or swim to the island\n").lower()
    if step2 == ('wait'):
        print("boat is here, It took you to the island")
        door = input("which door do you want to enter? red, blue or green\n").lower()
        if door == ('red'):
            print("oops you opened the chamber of python")
        elif door == ("blue"):
            print ("oops you opened the gate of rocks")
        elif door == ('green'):
            print("congratulations You won the treasure")
    elif step2 == ('swim'):
        print('Damm you are ripped apart by the crocodiles')
    else:
        print('please enter the correct response')

elif t == ('right'):
    print("oops you fell in a hole. try again")
else:
    print("please enter the the correct option")