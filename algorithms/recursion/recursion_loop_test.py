from unittest import TestCase

from .recursion_loop import loop


class TestRecursionLoop(TestCase):
    def test_simple(self) -> None:
        actual = list(loop([1, 2, 3, 4, 5]))
        expected = list(range(1, 6))
        self.assertEqual(expected, actual)
