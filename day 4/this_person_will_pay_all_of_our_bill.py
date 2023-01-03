names_string = input("Give me everyone's name in the group seprated with a comma")
names = names_string.split(",")
#method 1
x = len(names)

import random
z = random.randint(0, x-1)

q = names[z]

print(f"{q} will pay the bill")

# #alternate method
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + "is going to pay for the meal")