temp =  float(input("Enter Temperature :"))
unit = input("Celsius Or Fahrenheit ?( C or F ) :")

if unit == 'C':
    temp = round((9 * temp )/5  +32,2)
    unit = 'F'
    print(f"Temperature is {temp}{unit}")
elif unit =='F':
    temp = round((temp - 32) * 5 /9)
    unit = 'C'
    print(f"Temperature is {temp}{unit}")
else:
    print(f"{unit} is not valid unit ")
    unit = None
