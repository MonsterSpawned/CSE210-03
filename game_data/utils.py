# Authors: Bryan Hunter and Kent Lewis
from art import tprint
import os
from os.path import sep
import random
from game_data.word import Word
from sys import platform

class Utils():      
    
    def __init__(self):
        self.word = Word()
        self.guess_display = []
        self.current_platform = self.get_platform()
        
    def get_platform(self):
        print("Current platform: {}\n".format(platform.capitalize()))
        return platform.lower()
    
    def clear_console(self):
        command = 'cls' if os.name in ('nt', 'dos') else 'clear'
        os.system(command)
        
    # Chooses a word from the 'words.txt' file, randomly:
    def choose_word(self):
        word_file = open(os.getcwd() +  sep + "words.txt", "r")
        words = []
        words = word_file.readlines()
        length = len(words)
        self.word.selected_word = words[random.randint(0, length - 1)] 
        print(self.word.selected_word) # NOTE: This is a debug print call to tell us what the word the game has selected is. This will need to be removed when this is completed.
        return self.word.selected_word.strip("\n")

    # Prints the word guess list, wheel-of-fortune style:
    def print_guess_lines(self, selected_word):
        self.guess_display = ['_' for _ in selected_word]
        print(" ".join(self.guess_display))
    
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
            return _input
        print("Please input a valid letter and try again.")
        return None
    
    # TODO: Give feedback to the user based on the type of the scenario, hence the "scenario" variable. 
    # NOTE: The "user_guess" variable is optional, but can be used to pass through to the built feedback string as an argument.
    def get_feedback(self, scenario, user_guess="guess"):
        pass
