def convert (volume_in_gallons):
    volume_in_liters = volume_in_gallons * 3.785
    return volume_in_liters

volume_gallons=float(input("Enter volume in gallons: "))
while volume_gallons >0:
    volume_liters = convert(volume_gallons)
    print("The volume in liters is: ", volume_liters)
    volume_gallons=float(input("Enter volume in gallons: "))
