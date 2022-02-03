import random

class Word():
    
    pass # TODO: Load words from 'words.txt' into a list, randomly select one, and have that be the "word" for the instance of this class. 
    
    def __init__(self):
        self.selected_word = None

    def choose_word(self):
        words = open("words.txt", "r")
        content = []
        content = words.readlines()
        length = len(content)
        selected_word =random.randint(0, length - 1)
        # print(content[selected_word])   

    def guess_lines(self, selected_word):
        newguess = ('_ ' * len(selected_word))
        print(newguess)