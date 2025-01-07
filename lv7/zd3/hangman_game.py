from lv7.zd1.player import Player
from lv7.zd1.game_state_display import GameState
from lv7.zd2.hangman_points_calculator import HangmanPointsCalculator

class HangmanGame:
    def __init__(self, player_name: str, guess_word: str):
        self.__max_lives: int = 6
        self.__guess_word = guess_word
        self._guess_attempt = ""
        self.__player = Player(player_name, self.__max_lives)
        self.__display_tool = GameState()
        self.__points_calculator = HangmanPointsCalculator()

        # A class is missing some implementation details... TBD...