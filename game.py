from random import randint


class Game:
    def __init__(self, size=5):
        self.size = size
        self.board = [["O"] * self.size for _ in range(self.size)]
        self.ship_row = self.random_row()
        self.ship_col = self.random_col()
        self.turns = 4

    def print_board(self):
        print("   " + " ".join([str(i) for i in range(1, self.size + 1)]))
        for i, row in enumerate(self.board, start=1):
            print(f"{i}  " + " ".join(row))

    def random_row(self):
        return randint(1, self.size)

    def random_col(self):
        return randint(1, self.size)

    def play(self):
        print("Давайте сыграем в Морской бой!")
        self.print_board()

        for turn in range(self.turns):
            print(f"\nХод {turn + 1}/{self.turns}")

            guess_row = int(input("Угадайте номер строки: "))
            guess_col = int(input("Угадайте номер столбца: "))

            if guess_row == self.ship_row and guess_col == self.ship_col:
                print("Поздравляем! Вы потопили мой корабль!")
                break
            else:
                if (
                        guess_row < 1
                        or guess_row > self.size
                        or guess_col < 1
                        or guess_col > self.size
                ):
                    print("Упс, это не даже в океане.")
                elif self.board[guess_row - 1][guess_col - 1] == "X":
                    print("Вы уже угадали эту клетку.")
                else:
                    print("Вы промахнулись!")
                    self.board[guess_row - 1][guess_col - 1] = "X"

            self.print_board()

        else:
            print("Игра окончена. Вы использовали все ходы.")
            print(f"Корабль находился в строке {self.ship_row} и столбце {self.ship_col}.")


if __name__ == "__main__":
    game = Game()
    game.play()