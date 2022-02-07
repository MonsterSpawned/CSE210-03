# Authors: Bryan Hunter and Josh Liddiard
from time import sleep
from game_data.word import Word
from game_data.player import Player
from game_data.utils import Utils

class Game():
    def __init__(self):
        self.game_name = "JUMPER GAME"
        self.currentTurn = None
        self.utils = Utils()
        self.word = Word()
        self.player = Player()
    
    def startGame(self):
        self.utils.print_fancy(self.game_name + ":", "")
        print("Welcome to {}!\n\nIn this game you will seek to solve a puzzle by guessing the letters of the secret word, one at a time\n\nBe cautious, for when you lose, this man dies!\n\n".format(self.game_name))
        self.currentTurn = 0
        current_word = str(self.utils.choose_word())
        self.utils.print_guess_lines(current_word)
        self.handleRound()
        
    def handleRound(self):
        guess_state = True
        while guess_state:
            sleep(1)
            guess_state = self.utils.get_player_input("What letter would you like to guess? (Not case-sensitive): ")
            if guess_state == True:
                print("Correct!")
            else:
                print("Try again!")
        # TODO: Run an instance of each round here... :)

if __name__ == "__main__":
    print("\nStarting up...\n")
    game = Game()
    game.startGame()
    
