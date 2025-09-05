Number=(input("Enter the 1st  number or press 'Enter' to quit: "))
Numbers=[]

while Number != "":
    Numbers.append(int(Number))
    Number=(input("Enter a number or press 'Enter' to quit: "))

Numbers.sort(reverse=True)
print(Numbers[0:5])
