# Authors: Bryan Hunter and Kent Lewis
from art import tprint
import os
from os.path import sep
import random
from game_data.word import Word

class Utils():
    
    # TODO: Need a way to update the guess letter boxes (the Wheel of Fortune looking ones).       
    
    def __init__(self):
        self.word = Word()
    
    # Chooses a word from the 'words.txt' file, randomly:
    def choose_word(self):
        word_file = open(os.getcwd() +  sep + "words.txt", "r")
        words = []
        words = word_file.readlines()
        length = len(words)
        self.word.selected_word = words[random.randint(0, length - 1)] 
        print(self.word.selected_word) # NOTE: This is a debug print call to tell us what the word the game has selected is. This will need to be removed when this is completed.
        return self.word.selected_word  

    # Prints the word guess list, wheel-of-fortune style:
    def print_guess_lines(self, selected_word):
        word_len = len(selected_word) - 1
        self.guess_sub = ('_ ' * word_len)
        print(self.guess_sub)
    
    # Prints a fancy word in the console:
    def print_fancy(self, msg, font):
        if font != None:
            tprint(msg, font)
        else:
            tprint(msg)
    
    # Gets the player's guess input:
    def get_player_input(self, guess_input):    
        _input = str(input(guess_input)).lower()
        if _input.isalpha() != False:
            return _input in self.word.selected_word
        print("Please input a valid letter and try again.")
        return False
            
    def print_normal(msg):
        print("[LOG] " + msg)
