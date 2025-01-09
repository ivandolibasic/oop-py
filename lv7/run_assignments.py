from lv7.zd1.player import Player
from lv7.zd1.game_state_display import GameState
from lv7.zd2.hangman_points_calculator import HangmanPointsCalculator
from lv7.zd2.length_points_calculator import LengthPointsCalculator
from lv7.zd3.hangman_game import HangmanGame


# How to import modules https://www.learnpython.org/en/Modules_and_Packages

def run():
    #player = Player("Pero", 5)
    #game = GameState()
    #game.display(player.name, max(player.health_points, 6), player.health_points, "gt", "table")
    # Max function https://www.w3schools.com/python/ref_func_max.asp

    #base_calc = HangmanPointsCalculator(3, 2)
    #base_pts = base_calc.calculate_points("gt", "table", player)
    #print(f"Base calculator points: {base_pts}")

    #advanced_calc = LengthPointsCalculator(3, 2, 2)
    #advanced_pts = advanced_calc.calculate_points("gt", "table", player)
    #print(f"Advanced calculator points: {advanced_pts}")

    hangman_game = HangmanGame("Pero", "table")
    while not hangman_game.is_over():
        hangman_game.display()
        game_mode = input("Enter c for letter, w for word guess:\n")
        if game_mode.lower() == 'c':
            guess_letter = input("Enter letter:\n")
            hangman_game.letter_guess(guess_letter)
        else:
            guess_word = input("Guess word:\n")
            hangman_game.word_guess(guess_word)
    if hangman_game.has_won():
        print("Congrats, you won!")
    else:
        print(f"You lost. The guess word was: '{hangman_game.guess_word}'.")


run()