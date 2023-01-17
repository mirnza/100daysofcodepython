from art import logo
print(logo)
def addition(a1, a2):
    return a1 + a2
    
def subtraction(a1, a2):
    return a1 - a2

def multiplication(a1, a2):
    return a1 * a2

def division(a1, a2):
    return a1 / a2

operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division 
}

num1 = float(input("Whats the first number? : \n"))
num2 = float(input("Whats the second number? : \n"))

for symbol in operations:
    print(symbol)
s_symbol = input ("Pick a symbol: \n")
function = operations[s_symbol]
answer = function(a1= num1, a2=num2)
print(f"{num1} {s_symbol} {num2} is {answer}")
still_continue = True
while still_continue:
    x = input(f"Do you want to continue with {answer}? yes or no\n").lower()
    if x == "yes":
        s = input("Enter the symbol: \n")
        num3 = float(input("Whats the  number? : \n"))
        f2 = operations[s]
        answer = f2(a1=answer, a2 = num3)
        print(f"The answer is {answer}")
    elif x == "no":
        still_continue = False
    else:
        print("Invalid")



