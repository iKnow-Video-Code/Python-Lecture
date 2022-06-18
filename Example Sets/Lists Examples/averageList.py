# Average List Program - Program that calculates the average of numbers (can be int or double) in a list
# Average is the sum of values divided by number of values
# Use a combination of int and double values when declaring the list!

# Hint: sum(list) finds the sum of int/double values in a list
# len(list) finds the number of data items in a list)

listAverage = [1, 5, 6, 8.3, 3.5, 7.0]
print(sum(listAverage) / len(listAverage))

# Additional Challenge: Make the list contain both string and int/double values. Take only the average of int/double values
# The sum is adding the int/double values. The number to divide is the number of int/double values
# Reinitialize the variable to contain a string
# Use isinstance(value, primitive type) to determine if a value is some specific primitive type

listAverage = ["Arnesh", 1, 5, 6, 8.3, 3.5, 7.0, "This is a string"]
sumOfValues = 0
numOfValues = 0
for i in range(len(listAverage)):
    if isinstance(listAverage[i], int) or isinstance(listAverage[i], float):
        sumOfValues += listAverage[i]
        numOfValues += 1
print(sumOfValues / numOfValues)
