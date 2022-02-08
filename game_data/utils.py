# Authors: Bryan Hunter and Kent Lewis

# Custom imports (PIP packages):
from art import tprint

# Normal built-in packages:
import os
from os.path import sep
import random
from game_data.word import Word
from sys import platform
import string

class TextColors:
    # Text colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    PROMPT = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET_ALL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    CYAN = '\033[36m'
    BLUE = '\033[34m'
    BLACK = '\033[30m'
    # Background colors:
    GREYBG = '\033[100m'
    REDBG = '\033[101m'
    GREENBG = '\033[102m'
    YELLOWBG = '\033[103m'
    BLUEBG = '\033[104m'
    PINKBG = '\033[105m'
    CYANBG = '\033[106m'
    # Misc:
    BRIGHT = '\033[1m'
    NORMAL_BRIGHTNESS = '\033[22m'

class Utils():      
    
    def __init__(self):
        self.word = Word()
        self.guess_display = []
        self.current_platform = self.get_platform()
        self.tcolors = TextColors()
        
    def get_platform(self):
        print("Current platform: {}\n".format(platform.capitalize()))
        return platform.lower()
    
    def clear_console(self):
        command = 'cls' if os.name in ('nt', 'dos') else 'clear'
        os.system(command)
        
    # Chooses a word from the 'words.txt' file, randomly:
    def choose_word(self):
        word_file = open(os.getcwd() +  sep + "_words.txt", "r")
        words = []
        words = word_file.readlines()
        length = len(words)
        self.word.selected_word = words[random.randint(0, length - 1)] 
        print(self.word.selected_word) # NOTE: This is a debug print call to tell us what the word the game has selected is. This will need to be removed when this is completed.
        return self.word.selected_word.strip("\n")
    
    def get_current_word(self):
        return self.word.selected_word

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
            return str(_input)
        print("\n\n{}Please input a valid letter and try again.{}\n".format(self.tcolors.YELLOW, self.tcolors.RESET_ALL))
        return None
    
    # TODO: Give the player a letter for a hint from the "get_current_word()" function, which will be referenced in the "give_hint()" function in "_game.py":
    def get_random_letter_from_word(self):
        #a_z_lowercase = string.ascii_lowercase
        word_len = len(self.get_current_word())
        
        for item in self.get_current_word():
            print(item)
        
    def get_random_letter(self):
        letter_index = random.randint(min(self.word.selected_word), max(self.word.selected_word))
        return self.word.selected_word[letter_index]
        
    
    # TODO: Give feedback to the user based on the type of the scenario, hence the "scenario" variable. 
    # NOTE: The "user_guess" variable is optional, but can be used to pass through to the built feedback string as an argument.
    def get_feedback(self, scenario, user_guess="guess"):
        if scenario in ["miss", "wrong", "incorrect", 0]:
            if user_guess in ["guess", None]: 
                feedback = []
                return random.choice(feedback)
            else:
                guess_feedback = []
                return random.choice(guess_feedback)
        if scenario in ["correct", "right", 1]:
            if user_guess in ["guess", None]: 
                feedback = []
                return random.choice(feedback)
            else:
                guess_feedback = []
                return random.choice(guess_feedback)
        if scenario in ["win", "victory", 2]:
            feedback = []
            return random.choice(feedback)
        if scenario in ["quit", "exit", 3]:
            feedback = []
            return random.choice(feedback)
