Value_inch = float(input("Enter the value in inches : "))
while Value_inch >= 0:
    Value_cm = Value_inch * 2.54
    print(f"Value in cm : {Value_cm: .2f}")
    Value_inch=float(input("Enter the value in inches : "))
print("Invalid Inch Value")