from game_data.word import Word

class Player():
    # TODO: Hold player health here (if we want to measure it that way) and other stats here. Use as an instance for the "parachutist" for each round. 
    
    def __init__(self):
        self.word = Word()
        self.currentTurn = 0
        self.jumperHealth = 100

        guess = str(self.word.choose_word())
        self.word.print_guess_lines(guess)

        print(
            " _____\n"
            "/_____\ \n"
            "\     / \n"
            " \   / \n"
            "   0 \n"
            "  /|\ \n"
            "  / \ \n"
            "^^^^^^^\n")
        
        
