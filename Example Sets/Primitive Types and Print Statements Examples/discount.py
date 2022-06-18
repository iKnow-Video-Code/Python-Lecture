# Discount program - Program that calculates the discount price from a given price and discount percentage
# Create variable with normal cost, create variable with discount (represented in percent - exclude the percent sign when creating variable), and output the result

# Hint: Use round() function to round to two decimal places when we are dealing with prices
# Format to round() function: round(number you want to round, number of decimal places)
# So in this case, you would do round(price, 2)

cost = 54.40
discount = 36
print("The discount price is $" + str(round(cost - (discount / 100 * cost), 2)))