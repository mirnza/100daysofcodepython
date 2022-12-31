print("Welcome to leap year calculator!")

year = int(input("Enter the year that you want to check"))

#check the fellow diagram

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} os not a leap year")
    else:
        print(f"{year} is a leap year")

else:
    print(f'{year} is not a leap year')