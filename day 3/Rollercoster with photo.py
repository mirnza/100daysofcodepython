print("Welcome to the rollercoster!")
height = int(input("Enter your height here in cm:\n"))

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is your age?\n"))
    if age < 12:
       bill = 5
       print(f"Children tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    elif age >= 45 and age <= 55:
        print("Its all good you can ride for free")
    else:
        bill = 12
        print(f"Adult tickets are {bill}")

    photo = input("Do you want your photo take? Y or N\n")
    if photo == "Y":
        bill += 3
        print(f"Your total amount is ${bill}, please pay it at the counter")



else:
    print("You still need to grow up a little bit.")    