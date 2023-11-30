import random

class Hangman:
    def __init__(self, word_list,num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess, {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Please choose a single letter: ")
            if not guess.isalpha()==True and not len(guess)==1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                Hangman.check_guess(guess)
                
Hangman.ask_for_input("x")

