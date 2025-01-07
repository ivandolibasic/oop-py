class GameState:
    __full_heart: str
    __empty_heart: str

    def __init__(self, life_remaining_unit: str = "♥", life_taken_unit: str = "♡"):
        self.__full_heart = life_remaining_unit
        self.__empty_heart = life_taken_unit
    # Constructor overloading in Python
    # https://stackoverflow.com/questions/2164258/is-it-not-possible-to-define-multiple-constructors-in-python
    # https://realpython.com/python-multiple-constructors/

    def display(self, player_name: str, max_health_points: int, health_points: int, guess_attempt: str, guess_word: str) -> None:
        health: str = self.__full_heart * health_points + self.__empty_heart * (max_health_points - health_points)
        word_progress: str = ""
        for i in range(len(guess_word)):
            if guess_word[i] in guess_attempt:
                word_progress += guess_word[i]
            else:
                word_progress += "_"
        # Substring of a string https://www.learndatasci.com/solutions/python-string-contains/
        print(f"{player_name}: {health}\n{word_progress}")