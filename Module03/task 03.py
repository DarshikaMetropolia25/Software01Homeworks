gender = input("Enter your biological gender (Female or Male): ")
HB = float(input("Enter your hemoglobin value (g/l) : "))
if gender == "Female":
    if 117<= HB < 155:
        print("Your hemoglobin value is normal")
    elif 155 < HB:
        print("Your hemoglobin value is high")
    elif 117 > HB:
        print("Your hemoglobin value is low")
else:
    if 134<= HB < 167:
        print("Your hemoglobin value is normal")
    elif 167 < HB:
        print("Your hemoglobin value is high")
    elif 134 > HB:
        print("Your hemoglobin value is low")

