from random import randint

class Game:
    def __init__(self, size=5):
        self.size = size
        self.board = [["O"] * self.size for _ in range(self.size)]
        self.ship_row = None
        self.ship_col = None
        self.turns = 4

    def random_row(self):
        return randint(1, self.size)

    def random_col(self):
        return randint(1, self.size)


if __name__ == "__main__":
    game = Game()
