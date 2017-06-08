
class BowlingGame:

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        frame_index = 0
        while frame_index < len(self.rolls):
            if (self.is_spare(frame_index)):
                score += self.rolls[frame_index+2]

            score += self.rolls[frame_index] + self.rolls[frame_index+1]
            frame_index += 2

        return score

    def is_spare(self, frame_index):
        return ( self.rolls[frame_index] + self.rolls[frame_index + 1]== 10)



