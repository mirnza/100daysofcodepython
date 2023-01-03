rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random


print("Welcome to rock paper scissors game, press 0 for rock, 1 for paper and 2 scissors ")

x = int(input("Enter the no."))

if x == 0:
    print(rock)
elif x == 1:
    print(paper)
elif x == 2:
    print(scissors)

print("Computer chose:\n")
z = random.randint(0, 2)
if z == 0:
    print(rock)
elif z == 1:
    print(paper)
elif z == 2:
    print(scissors)

list = [x,z]
if list == [1,1]:
    print("its a draw")
elif list == [0,0]:
    print("its a draw")
elif list == [2,2]:
    print("its a draw")
elif list == [0,1]:
    print("computer wins")
elif list == [0,2]:
    print("you win")
elif list == [1,0]:
    print("you win")
elif list == [1,2]:
    print("Computer wins")
elif list == [2,0]:
    print("computer wins")
elif list == [2,1]:
    print("you win")


