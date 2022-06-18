# Letters Words Sentences Program - Program that calculates the number of letters, words, and sentences given user input
# Assume the user must input some punctuation (. or ! or ?) in order to count as a sentence

# Hint: Letters can be either lowercase or uppercase
# The number of words can be the number of whitespaces plus 1
# The number of sentences is only based off of the punctuation

textInput = input("Enter your text: ")
countLetters = 0
countWords = 1
countSentences = 0
for i in textInput:
    if i.islower() or i.isupper():
        countLetters += 1
    if i.isspace():
        countWords += 1
    if i == "?" or i == "!" or i == ".":
        countSentences += 1
print("The number of letters is " + str(countLetters))
print("The number of words is " + str(countWords))
print("The number of sentences is " + str(countSentences))