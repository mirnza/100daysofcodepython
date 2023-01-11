import math
test_h = int(input("Enter the height of the wall: \n"))
test_l = int(input("Enter the length of the wall: \n"))
coverage = 5
def paint_calc(height, length):
    calc = height * length / coverage
    calc = math.ceil(calc)
    print(f"You'll need {calc} cans of paint")

paint_calc(height = test_h, length=test_l)