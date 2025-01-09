from lv7.zd1.player import Player
from lv7.zd1.game_state_display import GameState
from lv7.zd2.hangman_points_calculator import HangmanPointsCalculator

class HangmanGame:
    def __init__(self, player_name: str, guess_word: str):
        self.__max_lives: int = 6
        self.__guess_word = guess_word
        self.__guess_attempt = ""
        self.__player = Player(player_name, self.__max_lives)
        self.__display_tool = GameState()
        self.__points_calculator = HangmanPointsCalculator()

    @property
    def guess_word(self):
        return self.__guess_word

    @property
    def points_calculator(self):
        return self.__points_calculator

    @property
    def player(self):
        return self.__player

    @property
    def guess_attempt(self):
        return self.__guess_attempt

    def display(self) -> None:
        self.__display_tool.display(self.__player.name,
                                    self.__max_lives,
                                    self.__player.health_points,
                                    self.__guess_attempt,
                                    self.__guess_word)

    def has_won(self) -> bool:
        for i in self.__guess_word:
            if i not in self.__guess_attempt:
                return False
        return True

    def has_lost(self) -> bool:
        return not self.__player.is_alive()

    def is_over(self) -> bool:
        return self.has_lost() or self.has_won()

    def letter_guess(self, letter: str) -> None:
        if letter in self.__guess_word and letter not in self.__guess_attempt:
            self.__guess_attempt += letter
        else:
            self.__player.reduce_health_points()

    def word_guess(self, word: str) -> None:
        if word == self.__guess_word:
            self.__guess_attempt = self.__guess_word
        else:
            self.__player.reduce_health_points()