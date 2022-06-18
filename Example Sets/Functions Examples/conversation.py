# Conversation Program - Program that involves a small conversation between you and the computer!
# There are two functions that you need to implement:
# 1. greet() function:
# The function prompts user to input their name. Then, the program prints out in the format "Hello (name)! Do you have a pet?". This function should call the answer() function that you are to implement next.
# 2. answer() function:
# The function prompts user to input an answer to the greet() function.
# If the answer is yes, the program prints out ":)". If the answer is no, the program prints out ":("
# Don't forget to call the greet() function after implementing the functions in order to actually put the function in action in our program!

def greet():
    name = input("What is your name? ")
    print("Hello " + name + "! Do you have a pet?")
    answer()

def answer():
    answer = input("What is your answer? ")
    if answer.lower() == "yes":
        print(":)")
    elif answer.lower() == "no":
        print(":(")

greet()