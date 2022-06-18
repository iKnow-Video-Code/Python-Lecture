# N Times N Program - Program that prints out a grid of N x N using a nested for loop

nTimesN = int(input("Enter your number to represent n: "))

for i in range(nTimesN):
    for j in range(nTimesN):
        print("N", end="")
    print()