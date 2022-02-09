# Authors: Bryan Hunter and Aitana (Invitado)

# Game classes:
from game_data.word import Word
from game_data.utils import TextColors
from game_data.parachutist_stages import ParachutistStages

class Player():
    
    # Initialize the Game() class:
    def __init__(self):
        self.stages = ParachutistStages()
        self.currentStage = self.stages.get_stage("first")
        self.wrongGuesses = 0
    
    # Print the current stage:
    def print_current_stage(self, current_stage):
        if current_stage in [1, 0, "first"]:
            print(self.stages.get_stage(current_stage).format(TextColors.WHITE, TextColors.RESET_ALL))
        if current_stage == 2:
            print(self.stages.get_stage(current_stage).format(TextColors.GREEN, TextColors.RESET_ALL))
        if current_stage == 3:
            print(self.stages.get_stage(current_stage).format(TextColors.CYAN, TextColors.RESET_ALL))
        if current_stage == 4:
            print(self.stages.get_stage(current_stage).format(TextColors.BLUE, TextColors.RESET_ALL))
        if current_stage == 5:
            print(self.stages.get_stage(current_stage).format(TextColors.YELLOW, TextColors.RESET_ALL))
        if current_stage in [6, "final", "last"]:
            print(self.stages.get_stage(current_stage).format(TextColors.RED, TextColors.RESET_ALL))
