from unittest import TestCase
from bowling_kata import BowlingGame

class TestBowlingGame(TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_gutter_game(self):
        for i in range (20):
            self.game.roll(0)

        self.assertEqual(0, self.game.score())


