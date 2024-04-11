height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

bmi = round(weight / (height ** 2), 1)

if bmi < 18.5:
    body_type = "underweight"
    weight_difference = round((18.5 - bmi) * (height ** 2))
    advice = f"You should gain approximately {weight_difference} kilograms to reach a healthy weight."
elif bmi >= 18.5 and bmi < 25:
    body_type = "normal weight"
    advice = "You are within a healthy weight range. Keep up the good work!"
elif bmi >= 25 and bmi < 30:
    body_type = "overweight"
    weight_difference = round((bmi - 25) * (height ** 2))
    advice = f"You should reduce approximately {weight_difference} kilograms to reach a healthy weight."
else:
    body_type = "obese"
    weight_difference = round((bmi - 25) * (height ** 2))
    advice = f"You should reduce approximately {weight_difference} kilograms to reach a healthy weight."

print("Your BMI is:", bmi)
print("Your body type is:", body_type)
print(advice)
