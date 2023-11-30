import random

word_list = ["apple","persimon","peach","raspberry","orange"]
"""List for random choice of word"""

word = random.choice(word_list)
"""Choice randomiser"""

"""def get_letter():
    #Code to repeatedly ask for an input which has to be 1 character long and a string character (letter)
    guess = input("Please enter a single letter: ")
    if guess.isalpha()==True and len(guess)==1:
     return print("Good guess")
    else:
     return print("Oops! That is not a valid input. Please try again: "),get_letter()
get_letter()"""

guess = input("Please enter a single letter: ")
if guess.isalpha()==True and len(guess)==1:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")

