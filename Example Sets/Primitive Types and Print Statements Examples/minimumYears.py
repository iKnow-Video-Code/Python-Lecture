# Minimum Years Program - Program that calculates the minimum number of years needed to buy a Tesla car and Apple watch
# Create variables - amount of money saved each month, cost of Tesla car, and cost of Apple watch (each in dollars)
# Note: minimum number of years can be a decimal/float!

# Hint: Find total cost of Tesla cars and Apple watch and perform some operation to determine the minimum number of years
# Convert from month to year (1 year = 12 months)


moneySavedEachMonth = 40
costTeslaCar = 50000
costAppleWatch = 250
totalCost = costTeslaCar + costAppleWatch
minimumMonths = totalCost / moneySavedEachMonth
minimumYears = minimumMonths / 12
print("The minimum number of years needed to buy the Tesla car and Apple watch is " + str(minimumYears))