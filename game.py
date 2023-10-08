class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(10)] for _ in range(10)]

    def place_ship(self, x, y, orientation, length):
        if orientation == 'horizontal':
            for i in range(length):
                self.board[x][y + i] = 'S'
            return True

