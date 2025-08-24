talent=float(input("Enter the Talent = "))
pound=float(input("Enter the Pound = "))
lot=float(input("Enter the Lot = "))
grams_talent=talent*20*32*13.3
grams_pound=pound*32*13.3
grams_lot=lot*13.3
total_grams=grams_talent+grams_pound+grams_lot
total_kilo=total_grams//1000
remain_grams=total_grams%1000
print(f"The weight in modern units")
print(f"{total_kilo: .0f} Kilograms and {remain_grams: .2f} grams")
