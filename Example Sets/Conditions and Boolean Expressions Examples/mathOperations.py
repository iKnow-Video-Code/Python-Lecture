# Mathematical Program - Program that involves mathematical addition, subtraction, multiplication, and division (operations)
# Prompt user to input two numbers, and prompt user to input operation to perform on the two inputted numbers
# Use conditions to check what operation the user typed in and print the output of operation used on the numbers 

firstNum = int(input("Enter your first number: "))
secondNum = int(input("Enter your second number: "))
operation = input("Enter your operation to perform on the numbers: ")
if operation == "+" or operation.lower() == "add":
    print(firstNum + secondNum)
elif operation == "-" or operation.lower() == "subtract":
    print(firstNum - secondNum)
elif operation == "*" or operation.lower() == "multiply":
    print(firstNum * secondNum)
elif operation == "/" or operation.lower() == "divide":
    print(firstNum / secondNum)
else:
    print("Invalid operation!")