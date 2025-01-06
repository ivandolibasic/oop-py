class GameState:
    __full_heart: str
    __empty_heart: str
    __guessing_word: str = "table"

    @property
    def full_heart(self):
        return self.__full_heart
    @property
    def empty_heart(self):
        return self.__empty_heart
    @full_heart.setter
    def full_heart(self, value):
        self.__full_heart = value
    @empty_heart.setter
    def empty_heart(self, value):
        self.__empty_heart = value
    @property
    def guessing_word(self):
        return self.__guessing_word
    @guessing_word.setter
    def guessing_word(self, value):
        self.__guessing_word = value

    def __init__(self, life_unit: str = "♥", death_unit: str = "♡"):
        self.__full_heart = life_unit
        self.__empty_heart = death_unit

    def display(self, name: str, max_health_points: int, health_points: int, current_guesses: str, guessing_word: str):
        life: str = self.full_heart * health_points + self.empty_heart * (max_health_points - health_points)
        word_progress: str = ""
        self.guessing_word = guessing_word
        for i in range(len(self.guessing_word)):
            if self.guessing_word[i] in current_guesses:
                word_progress += self.guessing_word[i]
            else:
                word_progress += "_"
        print(f"{name}: {life}\n{word_progress}")