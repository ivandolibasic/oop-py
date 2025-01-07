from lv7.zd2.hangman_points_calculator import HangmanPointsCalculator
from lv7.zd1.player import Player

class LengthPointsCalculator(HangmanPointsCalculator):
    def __init__(self, points_per_letter: int, points_per_life_remaining: int, length_points: int):
        super().__init__(points_per_letter, points_per_life_remaining)
        self.__length_points: int = length_points

    def calculate_points(self, guess_attempt: int, guess_word: str, player: Player):
        total_points: int = super().calculate_points(guess_attempt, guess_word, player)
        if player.health_points > 1:
            total_points += self.__length_points * len(guess_word)
        return total_points