# Divisible By Five Program - Program that determines the amount of numbers between 9 and 59 that are divisible by 5 using a while loop

# Hint: Use the modulo operator to determine if there is gonna be no remainder after dividing a number by 5 (no remainder = divisible)

amountOfNumbersDivisible = 0
startNumber = 9
while startNumber <= 59:
    if startNumber % 5 == 0:
        amountOfNumbersDivisible += 1
    startNumber += 1

print(amountOfNumbersDivisible)