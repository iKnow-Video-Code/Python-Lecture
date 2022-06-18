# Average List Expanded Program - Program that prompts user to input values to store in a list, then calculating the average of those values (expands on to the average list problem)
# The program prompts user to input values a certain amount of times (make sure to prompt the user to input the amount of values they want in the list before actually prompting user to input the values)
# Make sure that the user can input both int and double values

# Hint: an int can be considered a float since a float has a larger range which also includes int
# It is better to prompt user to input a float instead of int (users can still enter int values with float)

listOfValues = []
amountOfValues = int(input("Number of values you want to store in list: "))
for i in range(amountOfValues):
    valuesToEnter = float(input("Enter your values: "))
    listOfValues.append(valuesToEnter)

print(sum(listOfValues) / len(listOfValues))