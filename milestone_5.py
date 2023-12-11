import random
# imports the random function into python

class Hangman:
    """MAIN CLASS DEFINITION
    Setting variables and key features of the programme
    """
    
    def __init__(self, word_list,num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list) # chooses word at random from list of words
        self.word_guessed = list('_' * len(self.word)) # creates list of 'spaces' for game word
        self.num_letters = len(set(self.word)) # sets original number of unique letters to guess
        self.list_of_guesses = [] # so that the player knows if they have chosen the letter previously



    def check_guess(self,guess):
        """Checks to see if user input 'guess' is in the code
        Alters counters dependent on status of 'guess'"""

        guess = guess.lower() #converts the letter to lower case, one check instead of Upper and Lower
        if guess in self.word:
            print(f"Good guess, {guess} is in the word.")
            for letters in range(len(self.word)):
                if guess == self.word[letters]:
                    self.word_guessed[letters] = guess
                    # replaces the individual letters in the 'spaces' that match
            print(self.word_guessed)
            self.num_letters -= 1
            
        else: # if guess is not in the word
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")  
            

    def ask_for_input(self):
        """Starting point for the code to play the game
        notice that it is at the bottom so that everything else is created and organised before play actually commences"""
        
        while  True:
            guess = input("Please choose a single letter: ")
            if guess.isalpha()!=True or len(guess)!=1: # check to ensure guess is within the (letter) (single character) parameters
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses: # check if letter has been selected before
                print("You already tried that letter!")
            else:
                 self.list_of_guesses.append(guess) # add new letter to those that have been chosen
                 self.check_guess(guess) # call the next part of the process
                 break # ends the WHILE loop
            


def play_game(word_list): # word_list passed in from function call
    num_lives = 5 # sets number of lives available
    game = Hangman(word_list,num_lives) # pass word_list and number of lives to the main Class, and shorthand the class title

    while True:
        if game.num_lives == 0: # check the number of lives IN THE CLASS (not a local variable) 
            print("You lost!")
            break           
        elif game.num_letters >0: # does the player need to guess any more letters?
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!") # if the two above are not true, then player has won
            break
    
    
    


play_game(["apple","persimmon","peach","raspberry","orange"]) # call function and pass in list