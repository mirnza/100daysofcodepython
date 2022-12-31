height = float(input("Enter your height in m:\n"))
weight = float(input("Enter your height in KG: \n"))

BMI = weight/height**2
BMI = round(BMI, 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI} and you have a normal weight ")
elif BMI < 30:
    print(f"Your BMI is {BMI} and you are overweight ")
elif BMI < 35:
    print(f"Your BMI is {BMI} and you are obese ")
else:
    print(f"Your BMI is {BMI} and you are clinically obese ")
