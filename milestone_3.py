def check_guess(guess):
#word = "apple" #For testing purposes only
 word = set("apple")
 guess = guess.lower()
 if guess in word:
   print(f"Good guess, {guess} is in the word.")
 else:
   print(f"Sorry, {guess} is not in the word. Try again.") #, ask_for_input()


def ask_for_input():
    
    while True:
      guess = input("Please choose a single letter: ")
      if guess.isalpha()==True and len(guess)==1:
       break
      else:
       print("Invalid letter. Please, enter a single alphabetical character.")
       
    
    check_guess(guess)   







ask_for_input()