# Palindrome Program - Program that determines if a word (or even phrase) is a palindrome given user input
# A palindrome is basically a word (or phrase) that reads the same backwards as forwards
# A good example is racecar (reversed word is same as normal word)
# If there are phrases used, get rid of the whitespaces and count it as one word to determine if it is a palindrome

# Hint: Use the replace() method to replace all whitespaces with no whitespace
# This gives us the ability to keep phrases as one word and compare it to reversed word as one word making it easier to compare phrases
# Using the replace() method on words in order to replace all whitespaces with no whitespaces does not affect strings with only one word

promptUserInput = input("Enter your text: ").lower()
promptUserInputWithoutWhiteSpaces = promptUserInput.replace(" ", "")
reversedString = ""
for i in range(len(promptUserInputWithoutWhiteSpaces) - 1, -1, -1):
    reversedString += promptUserInputWithoutWhiteSpaces[i]

if promptUserInputWithoutWhiteSpaces == reversedString:
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")