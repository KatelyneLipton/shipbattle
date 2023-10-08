import unittest
from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_create_empty_board(self):
        self.assertEqual(len(self.game.board), 10)
        for row in self.game.board:
            self.assertEqual(len(row), 10)
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_place_ship(self):
        self.assertTrue(self.game.place_ship(0, 0, 'horizontal', 3))
        self.assertEqual(self.game.board[0][0], 'S')
        self.assertEqual(self.game.board[0][1], 'S')
        self.assertEqual(self.game.board[0][2], 'S')

if __name__ == '__main__':
    unittest.main()
