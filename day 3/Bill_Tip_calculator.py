print("Welcome to Bill calculator")
x = input("what is total amount of the bill?:\n")
x = float(x)
y = input("what percentage of tip do you want to pay? 10,12 or 15 :\n")
y = float(y)
z = input("how many members are in your group?\n")
z = float(z)

amount_to_pay = (x + x*y/100)/z

k = round(amount_to_pay, 2)

print(f"You have to pay {k} each.")