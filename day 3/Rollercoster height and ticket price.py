print("welcome to the the rollercoster")
height =int(input("Enter your height:\n"))

if height >= 120:
    print("You can ride on the rollercoster!")
    age = int(input("Enter your age:\n"))
    if age < 12:
        print("You need to pay $5 for the ticket")
    elif age <= 18 :
        print("You need to pay $7 for the ticket")
    else:
        print("you need to pay $12 for the ticket")
else:
    print ("You still need to grow up a little bit")