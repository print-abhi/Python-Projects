a = float(input("Enter 1st no. :"))
b = float(input("Enter 2nd no. :"))
c = input("Enter Operation ( + , - , * , / ) :")

if c == "+":
    print("Answer:",a + b)
elif c == "-":
    print("Answer:",a - b)
elif c == "*":
    print("Answer:",a * b)
elif c == "/":
    if b != 0:  # Prevent division by zero
        print("Answer:",a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("This operation is not valid.")
