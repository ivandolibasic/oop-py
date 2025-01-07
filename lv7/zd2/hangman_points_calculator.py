from lv7.zd1.player import Player

class HangmanPointsCalculator:
    def __init__(self, points_per_letter: int = 1, points_per_life_remaining: int = 1):
        self.__points_per_letter: int = points_per_letter
        self.__points_per_life_remaining: int = points_per_life_remaining

    def calculate_points(self, guess_attempt: str, guess_word: str, player: Player) -> int:
        if not player.is_alive():
            return 0
        letter_points: int = 0
        for letter in guess_attempt:
            if letter in guess_word:
                letter_points += self.__points_per_letter
        life_points = player.health_points * self.__points_per_life_remaining
        return letter_points + life_points