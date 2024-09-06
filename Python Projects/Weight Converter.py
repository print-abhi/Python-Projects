weight = float(input("Enter Your Weight :"))
unit = input("Kilogram or Pound ? (K or L) :" )

if unit == 'K':
    weight = weight * 2.205
    unit = "Lbs"
    print(f" Your Weight is {weight} {unit}")
elif unit =='L':
    weight = weight / 2.205
    unit = "kgs"
    print(f" Your Weight is {weight} {unit}")
else :
    print(f"{unit} is not a valid unit ")
    unit = None



    