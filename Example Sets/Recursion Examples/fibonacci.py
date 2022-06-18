# Fibonacci Program - Program that calculates the number within the fibonacci sequence (start counting at 0 within the sequence)
# Prompt user to input the certain position of the fibonacci sequence they want to calculate
# The Fibonacci Sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# In the Fibonacci Sequence, the number at a certain position is the sum of the two preceding numbers (starts at 0 and 1)

def fibonacci(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

promptUserInput = int(input("Enter the position of the fibonacci sequence you would like to calculate: "))
print("The number at this position in the fibonacci sequence is " + str(fibonacci(promptUserInput)))