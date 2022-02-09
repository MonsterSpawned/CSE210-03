# Authors: Bryan Hunter and Guage Schneider
import random
import os
from os.path import sep


class Word:
    # TODO: Load words from 'words.txt' into a list, randomly select one, and have that be the "word" for the instance of this class.

    def __init__(self):
        self.selected_word = ""
        self.guess_sub = []

        with open(os.getcwd() + sep + "words.txt", "r") as f:
            self.words = f.readlines()

    def choose_word(self):
        self.selected_word = random.choice(self.words)
        self.guess_sub = ["_" for _ in self.selected_word]
        return self.selected_word


    """ngl I'm a bit confused at what this is supposed to do.... Hence why it is commented out
    Let's please discuss on date of the meeting Thursday."""
    # def print_guess_lines(self, selected_word):
    #     word_len = len(selected_word) - 1
    #     self.guess_sub = ('_ ' * word_len)

    # print(" ".join(self.guess_sub))
    #     print(self.guess_sub)

    def check_guess(self, letter: str) -> bool:
        # Penis
        if len(letter) > 1:
            raise ValueError("Too many letters!")
        if letter not in self.selected_word:
            return False
        for i, word_letter in enumerate(self.selected_word):
            if letter == word_letter:
                self.guess_sub[i] = letter

        return True