h = int(input("Enter your Height (cm): "))
w = int(input("Enter your weight (kg): "))
h1 = h * 0.01
body = w / (h1*h1)
print("Your BMI = ",body,end = ' is ')
if body < 16:
    print("Severely Underweight")
elif body < 18.5:
    print("Underweight")
elif body < 25:
    print("Normal")
elif body < 30:
    print("Overweight")
else: print("Oberse")
