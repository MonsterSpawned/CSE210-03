import random
import os
from os.path import sep

class Word():
    # TODO: Load words from 'words.txt' into a list, randomly select one, and have that be the "word" for the instance of this class. 
    
    def __init__(self):
        self.selected_word = None
        self.guess_sub = None

    def choose_word(self):
        word_file = open(os.getcwd() +  sep + "words.txt", "r")
        words = []
        words = word_file.readlines()
        length = len(words)
        self.selected_word = words[random.randint(0, length - 1)] 
        print(self.selected_word) # NOTE: This is a debug print call to tell us what the word the game has selected is. This will need to be removed when this is completed.
        return self.selected_word  

    def print_guess_lines(self, selected_word):
        word_len = len(selected_word) - 1
        self.guess_sub = ('_ ' * word_len)
        print(self.guess_sub)
        
    