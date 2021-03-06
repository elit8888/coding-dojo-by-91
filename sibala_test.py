import unittest
from typing import List
from testfixtures import compare


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

    def inner_for(self, input_str: str) -> List[PlayerScore]:
        return [self.inner(s) for s in input_str.split("  ")]

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

    def test_from_input_two_2_player_scores(self):
        input_str = "Amy:2 2 6 6  Lin:6 6 3 1"
        expected = [PlayerScore("Amy", [2, 2, 6, 6]), PlayerScore("Lin", [6, 6, 3, 1])]
        res = SUT().inner_for(input_str)
        compare(expected, res)

if __name__ == '__main__':
    unittest.main()
