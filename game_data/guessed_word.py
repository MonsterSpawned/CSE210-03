# Authors: Josh Liddiard

class GuessedWord:
  # Acts as a holder to store the player's correct guesses and the remaining blanks in the word

    def __init__(self, word):
      # Initialize the guessed_word() class:
      self.guess_string=['_' for _ in word]
      self.guessed_letters=[]

    def get_guess_string(self):
      return self.guess_string
    
    def set_guess_string(self, guess, word):
      i=0
      for letter in word:
        if guess == letter:
          self.guess_string[i] = guess
        i += 1

    def get_guessed_letters(self):
      return self.guessed_letters

    def set_guessed_letters(self,letter):
      self.guessed_letters.append(letter)
