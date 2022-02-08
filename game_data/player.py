# Authors: Bryan Hunter and Aitana (Invitado)
from game_data.word import Word
from game_data.parachutist_stages import ParachutistStages

class Player():
    
    def __init__(self):
        self.currentStage = ParachutistStages.stage_1
        self.wrongGuesses = 0
        
    def print_current_stage(self, current_stage):
        if current_stage in [1, 0, "first"]:
            print(ParachutistStages.stage_1)
        if current_stage == 2:
            print(ParachutistStages.stage_2)
        if current_stage == 3:
            print(ParachutistStages.stage_3)
        if current_stage == 4:
            print(ParachutistStages.stage_4)
        if current_stage == 5:
            print(ParachutistStages.stage_5)
        if current_stage in [6, "final", "last"]:
            print(ParachutistStages.stage_6)
