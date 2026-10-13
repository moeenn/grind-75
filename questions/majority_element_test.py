from unittest import TestCase

from .majority_element import majority_element


class TestMajorityElement(TestCase):
    def test_simple(self) -> None:
        cases = [
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
            ([1, 2, 3, 1, 1, 4, 1], 1),
            ([-5, 3, -5, 3, -5], -5),
        ]

        for nums, expected in cases:
            self.assertEqual(expected, majority_element(nums))
