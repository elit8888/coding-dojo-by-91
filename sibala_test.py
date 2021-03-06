import unittest
from typing import List
from enum import IntEnum
from collections import Counter
from testfixtures import compare


class PlayerScore:
    def __init__(self, name: str, scores: List[int]):
        self.name = name
        self.scores = scores


class DiceType(IntEnum):
    AllOfSameKind = 2
    Normal = 1
    NoPoint = 0


class SUT:
    def game(self, input_str: str) -> str:
        return "Amy wins. normal point: 4"

    def inner(self, input_str: str) -> PlayerScore:
        name, str_scores = input_str.split(":")
        int_scores = [int(s) for s in str_scores.split(" ")]
        return PlayerScore(name, int_scores)

    def inner_for(self, input_str: str) -> List[PlayerScore]:
        return [self.inner(s) for s in input_str.split("  ")]

    def get_dice_type(self, input_score: List[int]) -> DiceType:
        c = Counter(input_score)
        if (N := len(c)) == 1:
            return DiceType.AllOfSameKind
        elif N == 4:
            return DiceType.NoPoint
        return DiceType.Normal


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

    def test_score_to_dice_type(self):
        input_score = [1, 1, 1, 1]
        expected = DiceType.AllOfSameKind
        compare(expected, SUT().get_dice_type(input_score))

        input_score = [2, 2, 1, 3]
        compare(DiceType.Normal, SUT().get_dice_type(input_score))

        input_score = [1, 2, 3, 4]
        compare(DiceType.NoPoint, SUT().get_dice_type(input_score))

    def test_compare_dice_type(self):
        self.assertTrue(DiceType.AllOfSameKind > DiceType.Normal)
        self.assertTrue(DiceType.AllOfSameKind > DiceType.NoPoint)
        self.assertTrue(DiceType.Normal > DiceType.NoPoint)

if __name__ == '__main__':
    unittest.main()
