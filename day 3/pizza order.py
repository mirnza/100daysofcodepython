# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
    price = 15
    if add_pepperoni == 'Y':
        price += 2
        if extra_cheese == 'Y':
            price += 1
    else:
        price = price
        if extra_cheese == 'Y':
            price += 1
    print(f"your total amount is ${price}")

elif size == 'M':
    price = 20
    if add_pepperoni == 'Y':
        price += 3
        if extra_cheese == 'Y':
            price += 1
    else:
        price = price
        if extra_cheese == 'Y':
            price += 1    
    print(f"your total amount is ${price}")

elif size == 'L':
    price = 25
    if add_pepperoni == 'Y':
        price += 3
        if extra_cheese == 'Y':
            price += 1
    else:
        price = price
        if extra_cheese == 'Y':
            price += 1
    print(f"your total amount is ${price}")

else:
    print("Please enter a valid entry.")


 