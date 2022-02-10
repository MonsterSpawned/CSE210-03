# Authors: Bryan Hunter and Josh Liddiard
from time import sleep
from game_data.guessed_word import GuessedWord
from game_data.word import Word
from game_data.player import Player
from game_data.utils import Utils, TextColors

class Game():
    
    # Initialize the Game() class:
    def __init__(self):
        self.utils = Utils()
        self.tcolors = TextColors()
        self.player = Player()
        self.word = Word()
        self.guessed_word = GuessedWord(self.word.get_selected_word())
        self.game_name = "Jumper Game"
        self.guesses=[]

    # Start the game:
    def start_game(self):
        self.utils.print_fancy(self.game_name + ":", "")
        print("Welcome to {}!\n\nIn this game you will seek to solve a puzzle by guessing the letters of the secret word, one at a time\n\nBe cautious, for when you lose, this man dies!\n\n".format(self.game_name))
        self.handle_round()
        self.play_again()
    
    # Handle one round of the game, then call self again if game end state is not reached:
    def handle_round(self):
        self.utils.print_guess_string(self.guessed_word.guess_string) #display any guessed characters and the empty blanks for the word
        self.player.print_current_stage(self.player.get_current_stage()) #display the current state of the jumper
        guess = self.utils.get_player_input("\n{}What letter would you like to guess? (Not case-sensitive): {}".format(self.tcolors.PROMPT, self.tcolors.RESET_ALL))
        #get the players guess and check if it has already been guessed
        if guess in self.guessed_word.get_guessed_letters():
            print("\n{}You have already guessed: '{}'.{}\n".format(self.tcolors.YELLOW, guess, self.tcolors.RESET_ALL))
            self.handle_round()
        else:
            self.guessed_word.set_guessed_letters(guess)
            try:
                self.guessed_word.set_guess_string(str(guess), str(self.word.get_selected_word()))
                if guess not in self.word.get_selected_word():
                    self.player.set_current_stage(int(self.player.get_current_stage())+1)
                    print("\n{}You guessed: '{}'. That's not a letter in the word.{}\n".format(self.tcolors.YELLOW, guess, self.tcolors.RESET_ALL)) #TODO: User friendly feedback, possibly in the form of a "get_feedback()" function in utils.py.
            except TypeError as error:
                print('{}[ERROR]: "{}"{}'.format(self.tcolors.RED, error, self.tcolors.RESET_ALL))
            if int(self.player.get_current_stage()) == 6:
                self.player.print_current_stage(self.player.get_current_stage())
                print("\n{}SPLAT! Game over.{}\n".format(self.tcolors.RED, self.tcolors.RESET_ALL))
                self.play_again()
            if "_" not in self.guessed_word.guess_string:
                self.utils.print_guess_string(self.guessed_word.guess_string) #display any guessed characters and the empty blanks for the word
                print("\n{}Victory! You guessed the word.{}\n".format(self.tcolors.GREEN, self.tcolors.RESET_ALL))
            else:
                self.handle_round()

    
    # Ask the user if they wish to play again:
    def play_again(self):
        _ask = input('Do you want to play again? (Y/N) ').upper()
        if _ask in ["YES", "Y"]:
            print("\nStarting up...\n")
            sleep(2)
            game = Game()
            game.start_game()
        elif _ask in ["NO", "N"]:
            print('\nThanks for playing {}! Come back soon!'.format(self.game_name))
            sleep(1)
            exit(0)

# Start the program:
if __name__ == "__main__":
    print("\nStarting up...\n")
    sleep(2)
    game = Game()
    game.start_game()