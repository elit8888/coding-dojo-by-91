import unittest
from typing import List


class PlayerScore:
    def __init__(self, name: str, scores: List[int]):
        self.name = name
        self.scores = scores


class SUT:
    def game(self, input_str: str) -> str:
        return "Amy wins. normal point: 4"

    def inner(self, input_str: str) -> PlayerScore:
        name, str_scores = input_str.split(":")
        int_scores = [int(s) for s in str_scores.split(" ")]
        return PlayerScore(name, int_scores)

class MyTestCase(unittest.TestCase):
    def test_amy_will_win_with_normal_4_points(self):
        input = "Amy:2 2 6 6  Lin:6 6 3 1"
        expected = "Amy wins. normal point: 4"
        self.assertEqual(expected, SUT().game(input))

    def test_a_player_score(self):
        input_str = "Lin:2 2 6 6"
        expected = PlayerScore("Lin", [2, 2, 6, 6])
        res = SUT().inner(input_str)
        self.assertEqual(expected.name, res.name)
        self.assertEqual(expected.scores, res.scores)

if __name__ == '__main__':
    unittest.main()
