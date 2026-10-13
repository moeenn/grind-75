from unittest import TestCase

from .climbing_stairs import climb_stairs


class TestClimbingStairs(TestCase):
    def test_simple(self) -> None:
        cases = [
            (2, 2),
            (3, 3),
            (4, 5),
        ]

        for n, expected in cases:
            self.assertEqual(expected, climb_stairs(n))
