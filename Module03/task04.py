Year = int(input("Enter the year: "))
if Year % 100 == 0:
    if Year % 400 == 0:
         print("This is a Leap Year")
    else:
        print("This is not a Leap Year")
elif Year % 4 == 0:
    print("This is a Leap Year")
else:
    print("This is not a Leap Year")






