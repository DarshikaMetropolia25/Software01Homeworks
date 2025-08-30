Number_List = []
Number01 = input("Enter a number(press enter to quit) : ")
while Number01.strip() != "":
    Number_List.append(int(Number01))
    Number01 = (input("Enter a number: "))
print("Smallest number is : ",min(Number_List))
print("Largest number is : ",max(Number_List))
