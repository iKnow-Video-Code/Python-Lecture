# Truth Table Program - Program that calculates the results of the truth table (boolean "and/or/not" logic)
# Prompt user to input logical operator, prompt user to input value(s), output results based on boolean logic
# If the logical operator is "and/or", prompt user to input 2 values
# If the logical operator is "not", prompt user to input 1 value
# Assume the user is going to input a valid logical operator and valid boolean values (true/false)
# Make sure to describe each step using comments!!!


# Prompt user to input logical operator
logicalOperator = input("Enter the logical operator: ").lower()

# Calculate result based on the logical operator "and"
if logicalOperator == "and":
    firstValueAnd = input("First boolean value: ").lower()
    secondValueAnd = input("Second boolean value: ").lower()
    if firstValueAnd == "false" or secondValueAnd == "false":
        print("The result is false!")
    else:
        print("The result is true!")

# Calculate result based on the logical operator "or"
elif logicalOperator == "or":
    firstValueOr = input("First boolean value: ").lower()
    secondValueOr = input("Second boolean value: ").lower()
    if firstValueOr == "true" or secondValueOr == "true":
        print("The result is true!")
    else:
        print("The result is false!")

# Calculate result based on the logical operator "not"
elif logicalOperator == "not":
    valueNot = input("Boolean value: ").lower()
    if valueNot == "true":
        print("The result is false!")
    else:
        print("The result is true!")