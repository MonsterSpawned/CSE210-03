# Authors: Bryan Hunter and Kent Lewis
from art import tprint

class Utils():
    
    # Prints a fancy word in the console:
    def print_fancy(msg, font):
        if font != None:
            tprint(msg, font)
        else:
            tprint(msg)
            
    def print_normal(msg):
        print("[LOG] " + msg)
