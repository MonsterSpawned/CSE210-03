# Authors: Bryan Hunter and Josh Liddiard
from time import sleep
from game_data.word import Word
from game_data.player import Player
from game_data.utils import Utils, TextColors

class Game():
    def __init__(self):
        self.game_name = "JUMPER GAME"
        self.currentTurn = None
        self.utils = Utils()
        self.tcolors = TextColors()
        self.player = Player()
        self.word = Word()
    
    def start_game(self):
        self.utils.print_fancy(self.game_name + ":", "")
        print("Welcome to {}!\n\nIn this game you will seek to solve a puzzle by guessing the letters of the secret word, one at a time\n\nBe cautious, for when you lose, this man dies!\n\n".format(self.game_name))
        # !!! TODO: Implement this!
        #print("If you need a hint, type 'HINT' (Not case-sensitive, w/o quotes).\n\nYou can only do this once per round, however, so choose wisely as to when to use it!\n")
        self.currentStage = 1
        self.handle_round()
        self.play_again()
    
    def handle_round(self): 
        self.player.print_current_stage(self.currentStage)
        self.word.print_guess_lines(self.word.get_selected_word())
        
        guesses = []
        
        print(self.word.get_selected_word())
        
        while True:
            guess = self.utils.get_player_input("\n{}What letter would you like to guess? (Not case-sensitive): {}".format(self.tcolors.PROMPT, self.tcolors.RESET_ALL))
            
            if guess in guesses:
                print("\n{}You have already guessed: '{}'.{}\n".format(self.tcolors.YELLOW, guess, self.tcolors.RESET_ALL))
            elif guess not in self.word.guess_display:
                try:
                    for pos in range(len(self.word.get_selected_word())):
                        if guess==self.word.get_selected_word()[pos]:
                            self.word.guess_display[pos]=guess
                    print("\n" + " ".join(self.word.guess_display) + "\n")
                    if guess not in self.word.get_selected_word():
                        self.currentStage += 1
                        self.player.print_current_stage(self.currentStage)
                        print("\n{}You guessed: '{}'. That's not a letter in the word.{}\n".format(self.tcolors.YELLOW, guess, self.tcolors.RESET_ALL)) #TODO: User friendly feedback, possibly in the form of a "get_feedback()" function in utils.py.
                        if self.currentStage == 6:
                            #self.player.print_current_stage(self.currentStage)
                            print("\n{}SPLAT! Game over.{}\n".format(self.tcolors.RED, self.tcolors.RESET_ALL))
                            break
                except TypeError as error:
                    print('{}[ERROR]: "{}"{}'.format(self.tcolors.RED, error, self.tcolors.RESET_ALL))
                if "_" not in self.word.guess_display:
                    print("\n{}Victory! You guessed the word.{}\n".format(self.tcolors.GREEN, self.tcolors.RESET_ALL))
                    break
            guesses.append(guess)
    
    def play_again(self):
        _ask = input('Do you want to play again? (Y/N) ').upper()
        if _ask in ["YES", "Y"]:
            self.word = Word()
            print()
            sleep(2)
            self.start_game()
        elif _ask in ["NO", "N"]:
            print('\nThanks for playing {}! Come back soon!'.format(self.game_name))
            sleep(1)
            exit(0)
    
if __name__ == "__main__":
    print("\nStarting up...\n")
    sleep(3)
    game = Game()
    game.start_game()
    
