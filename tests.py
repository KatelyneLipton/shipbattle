import unittest
from game import Game
from unittest.mock import patch
from io import StringIO

class TestGame(unittest.TestCase):

    def test_game_creation(self):
        game = Game()
        self.assertEqual(game.size, 5)

    def test_random_row(self):
        game = Game()
        row = game.random_row()
        self.assertTrue(1 <= row <= game.size)

    def test_print_board(self):
        game = Game()
        expected_output = "   1 2 3 4 5\n1  O O O O O\n2  O O O O O\n3  O O O O O\n4  O O O O O\n5  O O O O O\n"
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            game.print_board()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_play_win(self):
        game = Game(size=2)
        game.ship_row = game.ship_col = 1
        expected_output = "Давайте сыграем в Морской бой!\n   1 2\n1  O O\n2  O O\n\nХод 1/4\nУгадайте номер строки: 1\nУгадайте номер столбца: 1\nПоздравляем! Вы потопили мой корабль!\n"
        with patch("builtins.input", side_effect=["1", "1"]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = game.play()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            self.assertEqual(result, "Победа")

if __name__ == '__main__':
    unittest.main()
