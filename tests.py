import unittest
from game import Game

class TestGame(unittest.TestCase):

    def test_game_initialization(self):
        game = Game()
        self.assertEqual(game.size, 5)
        self.assertEqual(len(game.board), 5)
        for row in game.board:
            self.assertEqual(len(row), 5)
        self.assertIsNone(game.ship_row)
        self.assertIsNone(game.ship_col)
        self.assertEqual(game.turns, 4)

if __name__ == '__main__':
    unittest.main()

