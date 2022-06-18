# Dream Car Program - Program that determines if Moyer can buy his dream car
# Farmers should pick up ripe fruits and leave unripe fruits
# Based on number of ripe fruits picked up, there is a gain in profit
# Based on the profit, determine if Moyer can buy his dream car

costDreamCar = 40000
costOfFruitsEach = 20
fruitIsRipe = True
if fruitIsRipe:
    fruitsPickedUp = 2000
profitGained = fruitsPickedUp * costOfFruitsEach
if profitGained >= costDreamCar:
    print("Moyer can buy his dream car! :)")
else:
    print("Moyer can not buy this dream car :(")