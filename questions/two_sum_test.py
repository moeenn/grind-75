from dataclasses import dataclass
from unittest import TestCase

from .two_sum import Pair, two_sum


@dataclass(frozen=True)
class TwoSumTestCase:
    nums: list[int]
    target: int
    expected: list[Pair]


class TestTwoSum(TestCase):
    def test_cases(self) -> None:
        cases = [
            TwoSumTestCase([2, 7, 11, 15], 9, [Pair(0, 1)]),
            TwoSumTestCase([3, 2, 4], 6, [Pair(1, 2)]),
            TwoSumTestCase([3, 3], 6, [Pair(0, 1)]),
        ]

        for tc in cases:
            actual = two_sum(tc.nums, tc.target)
            self.assertEqual(actual, tc.expected)
