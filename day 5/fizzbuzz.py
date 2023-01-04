for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'fizzbuzz'
        print(number)
    elif number % 5 == 0:
        number = 'buzz'
        print(number)
    elif number % 3 == 0:
        number = 'fizz'
        print(number)
    else:
        print(number)