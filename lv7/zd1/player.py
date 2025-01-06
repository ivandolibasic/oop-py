class Player:
    __score: int = 0

    def __init__(self, name: str, health_points: int):
        self.__name = name
        self.__health_points = health_points

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        self.__score = value
    @property
    def name(self):
        return self.__name
    @property
    def health_points(self):
        return self.__health_points

    def reduce_health_points(self):
        if self.health_points > 0:
            self.health_points -= 1

    def is_alive(self) -> bool:
        return self.health_points > 0

    def add_points(self):
        self.score += 1