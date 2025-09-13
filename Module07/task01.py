seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of a month(1-12) : "))

if 1 <= month <= 12 :
    if month == 12 or month == 1 or month == 2:
        season = seasons[0]
    elif month == 3 or month == 4 or month == 5:
        season = seasons[1]
    elif month == 6 or month == 7 or month == 8:
        season = seasons[2]
    else:
        season = seasons[3]

    print("The season is", season)
else:
    print("Invalid month number. Please enter a number between 1 and 12.")


