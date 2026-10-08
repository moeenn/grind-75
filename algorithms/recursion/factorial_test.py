from unittest import TestCase

from .factorial import factorial


class TestFactorials(TestCase):
    def test_simple(self) -> None:
        result = factorial(5)
        self.assertEqual(result, 120)
