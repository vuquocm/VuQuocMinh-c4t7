heightcm = float(input("enter your height in centimeter "))
weight = float(input("enter your weigrht in kilogram "))
height = heightcm/100
BMI = weight/(height**2)
print("your BMI is", BMI)
if BMI < 16:
    print("you are severly underweight")
if 16 <= BMI < 18.5:
    print("you are underweight")
if 18.5 <= BMI < 25:
    print("your are normal")
if 25 <= BMI < 30:
    print("you are oveweight")
if 30 <= BMI:
    print("you are obese")