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
        self.word = Word()
        self.player = Player()
    
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
        self.current_word = str(self.utils.choose_word())
        self.utils.print_guess_lines(self.current_word)
        
        guesses = []
        
        while True:
            guess = self.utils.get_player_input("\n{}What letter would you like to guess? (Not case-sensitive): {}".format(self.tcolors.PROMPT, self.tcolors.RESET_ALL))

            if guess in ["hint".lower(), "help".lower()]:
                self.give_hint()
            
            if guess in guesses:
                print("\n{}You have already guessed: '{}'.{}\n".format(self.tcolors.YELLOW, guess, self.tcolors.RESET_ALL))
            elif guess not in self.utils.guess_display:
                try:
                    for pos in range(len(self.current_word)):
                        if guess==self.current_word[pos]:
                            self.utils.guess_display[pos]=guess
                    print("\n" + " ".join(self.utils.guess_display) + "\n")
                    if guess not in self.current_word:
                        self.currentStage += 1
                        self.player.print_current_stage(self.currentStage)
                        print("\n{}You guessed: '{}'. That's not a letter in the word.{}\n".format(self.tcolors.YELLOW, guess, self.tcolors.RESET_ALL)) #TODO: User friendly feedback, possibly in the form of a "get_feedback()" function in utils.py.
                        if self.currentStage == 6:
                            #self.player.print_current_stage(self.currentStage)
                            print("\n{}SPLAT! Game over.{}\n".format(self.tcolors.RED, self.tcolors.RESET_ALL))
                            break
                except TypeError as error:
                    print('{}[ERROR]: "{}"{}'.format(self.tcolors.RED, error, self.tcolors.RESET_ALL))
                if "_" not in self.utils.guess_display:
                    print("\n{}Victory! You guessed the word.{}\n".format(self.tcolors.GREEN, self.tcolors.RESET_ALL))
                    break
            guesses.append(guess)
    
    # I chose an nested function as it will allow us to use the variables inside this function that are only in this function.
    def give_hint(self, wof_help=False, single_letter=False): # TODO: Give the player a hint of what the word is, automatically (probably a single letter once they have lost a certain amount of lives)
        # NOTE: the "wof_help" variable will automagically input the letters R-S-T-L-N-E, without taking any health from the player if the letters don't exist.
        # These are the most common consanants for the English Language.
        # By default it is "False"
        self.utils.get_random_letter_from_word()

        # if single_letter: # TODO: Divide the function to either give the player a single letter hint, or to fill R-S-T-L-N-E without penalty if they don't exist.
        #     for pos in range(len(self.utils.get_current_word())):
        #         if guess==self.utils.get_current_word()[pos]:
        #             self.utils.guess_display[pos]=guess
        # elif wof_help:
        #     for pos in range(len(self.utils.get_current_word())):
        #         if guess==self.utils.get_current_word()[pos]:
        #             self.utils.guess_display[pos]=guess
    
    def play_again(self):
        _ask = input('Do you want to play again? (Y/N) ').upper()
        if _ask in ["YES", "Y"]:
            print()
            sleep(2)
            self.handle_round()
        elif _ask in ["NO", "N"]:
            print('\nThanks for playing {}! Come back soon!'.format(self.game_name))
            sleep(1)
            exit(0)
    
if __name__ == "__main__":
    print("\nStarting up...\n")
    sleep(3)
    game = Game()
    game.start_game()
    
