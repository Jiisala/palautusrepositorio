
class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

