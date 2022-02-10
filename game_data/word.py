# Authors: Bryan Hunter and Guage Schneider
import random
import os
from os.path import sep


class Word:

    # Initialize the Word() class:
    def __init__(self):
        self.selected_word = ""
        self.words = []
        
        with open(os.getcwd() + sep + "_words.txt", "r") as f:
            self.words = f.readlines()
            length = len(self.words)
            self.selected_word = self.words[random.randint(0, length - 1)].strip("\n")

    # Gets the currently selected word by the game:   
    def get_selected_word(self):
        return self.selected_word