#variables
num1 = float(input("Enter a number:"))
num2 = float(input("Enter a second number:"))
operator = input("Enter the operator: ")

# simple addition
if operator == "+":
    print(num1 + num2)
# subtraction
elif operator == "-":
    print(num1 - num2)
# multiplication
elif operator == "*":
    print(num1 * num2)
# division
elif operator == "/":
    print(num1 / num2)

else:
    print("Invalid input!")
