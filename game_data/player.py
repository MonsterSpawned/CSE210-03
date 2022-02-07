# Authors: Bryan Hunter and Aitana (Invitado)
from game_data.word import Word
from game_data.parachutist_stages import ParachutistStages

class Player():
    # TODO: Print the stages each time the player guesses wrong (which is held in the 'utils.py' and '_game.py' code).
    
    def __init__(self):
        self.currentStage = ParachutistStages.stage_1
        self.wrongGuesses = 0
        
        
