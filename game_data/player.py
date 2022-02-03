from word import Word

class Player():
    pass # TODO: Hold player health here (if we want to measure it that way) and other stats here. Use as an instance for the "parachutist" for each round. 
    
    def __init__(self):
        word = Word
        self = 0
        print("Welcome to JUMPER GAME. In this game you will seek to solve a puzzle by guessing the letters of the secret word, one at a time.\n"
            "\n Be cautiuos, for when you lose, the man dies! \n ")

        name = input('Enter your nickname: ').capitalize()
        print(f"Let's start, {name}!\n")

        guess = str(word.choose_word(self))
        word.guess_lines(self, guess)

        print(
            " _____\n"
            "/_____\ \n"
            "\     / \n"
            " \   / \n"
            "   0 \n"
            "  /|\ \n"
            "  / \ \n"
            "^^^^^^^^")
        
        
