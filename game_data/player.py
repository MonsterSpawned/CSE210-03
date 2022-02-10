# Authors: Bryan Hunter and Aitana (Invitado)

# Game classes:
from game_data.utils import TextColors
from game_data.parachutist_stages import ParachutistStages

class Player():
    
    # Initialize the Player() class:
    def __init__(self):
        self.currentStage = 1
        self.stages = ParachutistStages()

    # Get the current round:
    def get_current_stage(self):
        return int(self.currentStage)
    
    # Set the current stage:
    def set_current_stage(self, stage):
        self.currentStage = stage
    
    # Show the state of the jumper:
    def print_current_stage(self, current_stage):
        if current_stage ==1:
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
