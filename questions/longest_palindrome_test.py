from unittest import TestCase

from .longest_palindrome import longest_palindrome


class TestLongestPalindrome(TestCase):
    def test_simple(self) -> None:
        cases = [
            ("abccccdd", 7),
            ("a", 1),
            ("aabb", 4),
            ("zzZZyyYY", 8),
        ]

        for input, expected in cases:
            self.assertEqual(expected, longest_palindrome(input))
