Number=int(input("Enter an integer: "))
Remainders=[]
if Number>1:
    for a in range (Number):
        Remainder = Number % (a+1)
        if Remainder==0:
            Remainders.append(Remainder)

    if len(Remainders)==2:
        print("This is a prime number.")
    else:
        print("This is not a prime number.")
else:
    print("This is a prime number.")






