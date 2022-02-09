# Authors: Bryan Hunter and Guage Schneider
import random
import os
from os.path import sep


class Word:
    # TODO: Load words from 'words.txt' into a list, randomly select one, and have that be the "word" for the instance of this class.

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
    
    """ngl I'm a bit confused at what this is supposed to do.... Hence why it is commented out
    Let's please discuss on date of the meeting Thursday."""
    # def print_guess_lines(self, selected_word):
    #     word_len = len(selected_word) - 1
    #     self.guess_sub = ('_ ' * word_len)

    # print(" ".join(self.guess_sub))
    #     print(self.guess_sub)
    def get_selected_word(self):
        return self.selected_word
    
    def check_guess(self, letter: str):
        if len(letter) > 1:
            raise ValueError("Too many letters!")
        if letter not in self.selected_word:
            return False
        for i, word_letter in enumerate(self.selected_word):
            if letter == word_letter:
                self.guess_sub[i] = letter

        return True