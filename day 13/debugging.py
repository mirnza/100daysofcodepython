# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You've done it")

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You've done it")
my_function()
# range function wasn't used perfectly in the above code.

# reproduce the bug
# from random import randint
# dice_img = ['1', '2', '3', '4', '5', '6']
# dice_num = randint(1,6)
# print(dice_img[dice_num])

from random import randint
dice_img = ['1', '2', '3', '4', '5', '6']
dice_num = randint(0,5)
print(dice_img[dice_num])

# play computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

year = int(input("what is your birth year?"))
if year > 1980 and year <= 1994:
    print("You're a millenial")
elif year > 1994:
    print("You're a gen z")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])