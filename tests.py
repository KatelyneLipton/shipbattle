import unittest
from game import Game

class TestGame(unittest.TestCase):

    def test_game_creation(self):
        game = Game()
        self.assertEqual(game.size, 5)

    def test_random_row(self):
        game = Game()
        row = game.random_row()
        self.assertTrue(1 <= row <= game.size)

if __name__ == '__main__':
    unittest.main()
