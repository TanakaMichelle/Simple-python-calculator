
print("Instructions: Enter \"+\" for addition, \"*\" for multiplication, \"/\"for division,"
      " \"-\" for subtraction.")


user_input = input("Enter your desired operation: ")
num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")

# simple addition
if user_input == "+":
    ans = float(num1) + float(num2)
    print("The answer is: ", ans)

# simple subtraction
elif user_input == "-":
    ans = float(num1) - float(num2)
    print("The answer is: ", ans)

# simple multiplication
elif user_input == "*":
    ans = float(num1) * float(num2)
    print("The answer is: ", ans)

# simple division
elif user_input == "/":
    ans = float(num1) / float(num2)
    print("The answer is: ", ans)

else:
    print("Invalid input")
