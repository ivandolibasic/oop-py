class Player:
    __name: str
    __health_points: int = 6
    __score: int = 0

    def __init__(self, name: str, health_points: int):
        self.__name = name
        self.__health_points = health_points

    @property
    def name(self):
        return self.__name
    @property
    def health_points(self):
        return self.__health_points

    def reduce_health_points(self) -> None:
        if self.__health_points > 0:
            self.__health_points -= 1

    def is_alive(self) -> bool:
        return self.__health_points > 0

    def add_points(self) -> None:
        self.__score += 1