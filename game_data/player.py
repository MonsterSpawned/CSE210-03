# Authors: Bryan Hunter and Aitana (Invitado)
from game_data.word import Word
from game_data.parachutist_stages import ParachutistStages


class Player:
    # TODO: Hold player health here (if we want to measure it that way) and other stats here. Use as an instance for the "parachutist" for each round.

    def __init__(self):
        self.currentStage = ParachutistStages.stage_1
        self.wrongGuesses = 0
