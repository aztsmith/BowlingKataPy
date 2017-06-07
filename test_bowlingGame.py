from unittest import TestCase
from bowling_kata import BowlingGame

class TestBowlingGame(TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_gutter_game(self):
        self.roll_many(20,0)
        self.assertEqual(0, self.game.score(), "test_gutter_game failed")

    def test_roll_all_ones(self):
        self.roll_many(20,1)
        self.assertEqual(20, self.game.score(), "test_roll_all_ones failed")

    def roll_many(self, number_of_rolls, pins):
        for i in range(number_of_rolls):
            self.game.roll(pins)


