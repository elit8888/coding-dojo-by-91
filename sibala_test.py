import unittest
from typing import List, Tuple
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
        val = self.inner_for(input_str)
        p1, p2 = val[0], val[1]
        p1_val = self.get_dice_type(p1.scores)
        p2_val = self.get_dice_type(p2.scores)
        if p1_val[0] == p2_val[0] == DiceType.Normal:
            p1_score, p2_score = p1_val[1], p2_val[1]
            if p1_score > p2_score:
                return f"{p1.name} wins. normal point: {p1_score}"
        return "Amy wins. normal point: 4"

    def inner(self, input_str: str) -> PlayerScore:
        name, str_scores = input_str.split(":")
        int_scores = [int(s) for s in str_scores.split(" ")]
        return PlayerScore(name, int_scores)

    def inner_for(self, input_str: str) -> List[PlayerScore]:
        return [self.inner(s) for s in input_str.split("  ")]

    def get_score_from_normal(self, c: Counter) -> int:
        res = 0
        for k, v in c.items():
            if v == 1:
                res += k
        return res

    def get_score_from_normal2(self, c: Counter) -> int:
        elem = list(c.keys())
        return max(elem) * 2

    def get_dice_type(self, input_score: List[int]) -> Tuple[DiceType, int]:
        c = Counter(input_score)
        if (N := len(c)) == 1:
            return (DiceType.AllOfSameKind, list(c.keys())[0])
        elif N == 4:
            return (DiceType.NoPoint, 0)
        elif N == 2:
            return (DiceType.Normal, self.get_score_from_normal2(c))
        return (DiceType.Normal, self.get_score_from_normal(c))


class MyTestCase(unittest.TestCase):
    def test_amy_will_win_with_normal_4_points(self):
        input = "Amy:2 2 6 6  Lin:6 6 3 1"
        expected = "Amy wins. normal point: 12"
        self.assertEqual(expected, SUT().game(input))

    def test_lin_will_win_with_normal_4_points(self):
        input = "Lin:2 2 6 6  Amy:6 6 3 1"
        expected = "Lin wins. normal point: 12"
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

    def test_compare_dice_type(self):
        self.assertTrue(DiceType.AllOfSameKind > DiceType.Normal)
        self.assertTrue(DiceType.AllOfSameKind > DiceType.NoPoint)
        self.assertTrue(DiceType.Normal > DiceType.NoPoint)

    def test_score_to_dice_type_with_value(self):
        input_score = [1, 1, 1, 1]
        compare((DiceType.AllOfSameKind, 1), SUT().get_dice_type(input_score))

        input_score = [2, 2, 1, 3]
        compare((DiceType.Normal, 4), SUT().get_dice_type(input_score))

        input_score = [2, 2, 6, 6]
        compare((DiceType.Normal, 12), SUT().get_dice_type(input_score))

        input_score = [1, 2, 3, 4]
        compare((DiceType.NoPoint, 0), SUT().get_dice_type(input_score))

    def test_dice_normal_type_to_compare(self):
        pass


if __name__ == '__main__':
    unittest.main()
