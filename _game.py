# Authors: Bryan Hunter and Josh Liddiard
from game_data.word import Word
from game_data.player import Player
from game_data.utils import Utils

class Game():
    def __init__(self):
        self.game_name = "JUMPER GAME"
    
    def startGame(self):
        Utils.print_fancy(self.game_name + ":", "")
        print("Welcome to {}!\n\nIn this game you will seek to solve a puzzle by guessing the letters of the secret word, one at a time\n\nBe cautious, for when you lose, this man dies!\n\n".format(self.game_name))
        self.player = Player()
        self.currentTurn = 0
        guess = str(self.word.choose_word())
        self.word.print_guess_lines(guess)
        self.word = Word()
        self.handleRound()
        
    def handleRound(self):
        pass # TODO: Run an instance of each round here... :)

if __name__ == "__main__":
    print("\nStarting up...\n")
    game = Game()
    game.startGame()
    
