# Halloween Party Program - Program that keeps track of the number of guests in a Halloween party
# The maximum (highest) number of guests that can be at a party is 50
# Everytime a guest, or group of guests, attends the party, keep track of the count to make sure that the number of guests does not surpass the capacity (number of guests)
# If there are no more guests coming, start the Halloween contest

numberOfGuests = 0
while numberOfGuests <= 50:
    addGuests = int(input("How many people are joining the party? "))
    numberOfGuests += addGuests
    if numberOfGuests > 50:
        print("You can not have over 50 guests! The number of guests is now at 50!")
        numberOfGuests = 50
        break
    print("You are at " + str(numberOfGuests) + " guests right now!")
    noMoreGuests = input("Are there going to be any more guests? ").lower()
    if noMoreGuests == "no":
        break

print("The Halloween Contest has started! There are " + str(numberOfGuests) + " guests right now!")