from unittest import TestCase

from .valid_palindrome import valid_palindrom


class TestValidPalindrome(TestCase):
    def test_valid(self) -> None:
        result = valid_palindrom("A man, a plan, a canal: Panama")
        self.assertTrue(result)

    def test_invalid(self) -> None:
        result = valid_palindrom("race a car")
        self.assertFalse(result)

    def test_blank(self) -> None:
        result = valid_palindrom(" ")
        self.assertTrue(result)
