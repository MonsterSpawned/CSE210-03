from game_data.word import Word
from game_data.parachutist_stages import ParachutistStages

class Player():
    # TODO: Hold player health here (if we want to measure it that way) and other stats here. Use as an instance for the "parachutist" for each round. 
    
    def __init__(self):
        self.word = Word()
        self.currentTurn = 0

        guess = str(self.word.choose_word())
        self.word.print_guess_lines(guess)

        print(ParachutistStages.stage_1)
        
        
