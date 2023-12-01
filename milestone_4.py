import random


class Hangman:
    
    def __init__(self, word_list,num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess, {guess} is in the word.")
           # print(self.word_guessed)
            for letters in range(len(self.word)):
                if guess == self.word[letters]:
                    self.word_guessed[letters] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"you have {self.num_lives} lives left")    

    def ask_for_input(self):
        
        while  True:
            guess = input("Please choose a single letter: ")
            if guess.isalpha()!=True or len(guess)!=1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                 self.list_of_guesses.append(guess)
                 self.check_guess(guess)
                 break
            

hangman = Hangman(["apple","persimon","peach","raspberry","orange"])
hangman.ask_for_input()
