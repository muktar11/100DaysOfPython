weight = float(input("enter your weight"))
height = float(input("enter your height"))
BMI = round(weight / height  ** 2)

if BMI < 18.5: 
    print(f" your bmi is {BMI} underweight")
elif  BMI < 25:
    print(f"you bmi is {BMI} normal weight")
elif BMI < 30: 
    print(f'your bmi is {BMI} Overweight')
elif  BMI < 35: 
    print(f"your bmi is {BMI} Obese")
else: 
    print(f"Clinical Obese")