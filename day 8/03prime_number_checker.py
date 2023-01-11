n = int(input("Check This number: \n"))
def prime_num(number):
    prime_is = True
    for i in range(2, number):
        if number % i == 0:
            prime_is == False
    if prime_is:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
prime_num(number=n)
    
