# Authors: Bryan Hunter and Guage Schneider
import random
import os
from os.path import sep


class Word:

    # Initialize the Word() class:
    def __init__(self):
        self.selected_word = ""
        self.guess_sub = []
        self.words = []
        
        with open(os.getcwd() + sep + "_words.txt", "r") as f:
            self.words = f.readlines()
            length = len(self.words)
            self.selected_word = self.words[random.randint(0, length - 1)].strip("\n")

    # Prints the word guess list, wheel-of-fortune style:
    def print_guess_lines(self, selected_word):
        self.guess_display = ['_' for _ in selected_word]
        print(" ".join(self.guess_display))
    
    # Gets the currently selected word by the game:   
    def get_selected_word(self):
        return self.selected_word
    
    # Checks to make sure only one letter was inputted:
    def check_guess(self, letter):
        if len(letter) > 1:
            raise ValueError("Too many letters!")
        if letter not in self.selected_word:
            return False
        for i, word_letter in enumerate(self.selected_word):
            if letter == word_letter:
                self.guess_sub[i] = letter

        return True