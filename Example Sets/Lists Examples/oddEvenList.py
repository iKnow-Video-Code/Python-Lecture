# Odd Even List Program - Program that finds the number of odd and even numbers and finds the difference between the number of odd and even numbers
# The difference has to be positive

# Hint: Use abs() to find the absolute value of number (absolute value will find the distance from number to 0, absolute value is always positive!!)

oddEvenList = [3, 6, 2, 8, 11, 10, 15]
countOdd = 0
countEven = 0
for i in range(len(oddEvenList)):
    if oddEvenList[i] % 2 == 1:
        countOdd += 1
    else:
        countEven += 1
print(abs(countOdd - countEven))