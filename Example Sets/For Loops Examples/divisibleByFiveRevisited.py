# Divisible By Five Revisited Program - Program that determines the amount of numbers between 9 and 59 that are divisible by 5 using a for loop

# Hint: Use the modulo operator to determine if there is gonna be no remainder after dividing a number by 5 (no remainder = divisible)

amountOfNumbersDivisible = 0
for startNumber in range(9, 60):
    if startNumber % 5 == 0:
        amountOfNumbersDivisible += 1

print(amountOfNumbersDivisible)