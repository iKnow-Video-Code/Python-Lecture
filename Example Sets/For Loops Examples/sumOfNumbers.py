# Sum Of Numbers Program - Program that calculates the sum of a number and all of its preceding numbers till 1, given user input
# For example, if 5 is user input, calculate 5 + 4 + 3 + 2 + 1

numberToCalculate = int(input("Enter your number: "))
calculatedNumber = 0
for i in range(numberToCalculate + 1):
    calculatedNumber += i

print(calculatedNumber)