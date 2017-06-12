from unittest import TestCase
from bowling_kata import BowlingGame

class TestBowlingGame(TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, number_of_rolls, pins):
        for i in range(number_of_rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def test_gutter_game(self):
        self.roll_many(20,0)
        self.assertEqual(0, self.game.score(), "test_gutter_game failed")

    def test_all_ones(self):
        self.roll_many(20,1)
        self.assertEqual(20, self.game.score(), "test_roll_ones failed")

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17,0)
        self.assertEqual(16,self.game.score(), "test_one_spare failed")

    # def test_one_strike(self):
    #     self.game.roll(10)
    #     self.game.roll(3)
    #     self.game.roll(4)
    #     self.roll_many(17,0)
    #     self.assertEqual(24, self.game.score(), "test_one_strike failed")





