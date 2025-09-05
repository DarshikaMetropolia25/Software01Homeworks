import math
def unit_rate_pizza(diameter,price):
   rate=price/(math.pi*((diameter/100)/2) ** 2)
   return rate

diameter=float(input("Enter the diameter of the pizza 01 in cm : "))
price=float(input("Enter the price of the pizza 01 in euro :  "))
rate_01 = unit_rate_pizza(diameter,price)

diameter=float(input("Enter the diameter of the pizza 02 in cm : "))
price=float(input("Enter the price of the pizza 02 euro : "))
rate_02 = unit_rate_pizza(diameter,price)

if rate_01 > rate_02:
    print("Pizza 02 is cheaper than pizza 01")
else:
    print("Pizza 01 is cheaper than pizza 02")



