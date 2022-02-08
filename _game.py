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
    
    def start_game(self):
        self.utils.print_fancy(self.game_name + ":", "")
        print("Welcome to {}!\n\nIn this game you will seek to solve a puzzle by guessing the letters of the secret word, one at a time\n\nBe cautious, for when you lose, this man dies!\n\n".format(self.game_name))
        self.currentStage = 1
        self.handle_round()
        self.play_again()
    
    def handle_round(self):
        self.player.print_current_stage(self.currentStage)
        current_word = str(self.utils.choose_word())
        self.utils.print_guess_lines(current_word)
        
        guesses = []
        
        while True:
            guess = self.utils.get_player_input("\nWhat letter would you like to guess? (Not case-sensitive): ")

            if guess in guesses:
                print("\nYou have already guessed: {}\n".format(guess))
            elif guess not in self.utils.guess_display:
                for pos in range(len(current_word)):
                    if guess==current_word[pos]:
                        self.utils.guess_display[pos]=guess
                print(" ".join(self.utils.guess_display) + "\n")
                if guess not in current_word:
                    self.currentStage += 1
                    self.player.print_current_stage(self.currentStage)
                    print(f"\nYou guessed: '{guess}'. That's not a letter in the word.\n") #TODO: User friendly feedback, possibly in the form of a "get_feedback()" function in utils.py.
                    if self.currentStage == 6:
                        self.player.print_current_stage(self.currentStage)
                        print("\nSPLAT! Game over.\n")
                        break
                if "_" not in self.utils.guess_display:
                    print("\nVictory! You guessed the word.\n")
                    break
            guesses.append(guess)

    def play_again(self):
        _ask = input('Do you want to play again? (Y/N) ').upper()
        if _ask in ["YES".upper(), "Y".upper()]:
            print()
            sleep(2)
            self.start_game()
        elif _ask in ["NO".upper(), "N".upper()]:
            print(f'Thanks for playing in {self.game_name}!')

if __name__ == "__main__":
    print("\nStarting up...\n")
    sleep(3)
    game = Game()
    game.start_game()
    
