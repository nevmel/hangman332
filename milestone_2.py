import random

def get_letter():
    guess = input("Please enter a single letter: ")
    if guess.isalpha()==True and len(guess)==1:
     return print("Good guess")
    else:
     return print("Oops! That is not a valid input. Please try again: "),get_letter()



word_list = ["apple","persimon","peach","raspberry","orange"]
print(word_list)

word = random.choice(word_list)
print(word)


get_letter()

