from unittest import TestCase

from .valid_anagram import valid_anagram


class TestValidAnagram(TestCase):
    def test_valid(self) -> None:
        self.assertTrue(valid_anagram("anagram", "nagaram"))

    def test_invalid(self) -> None:
        self.assertFalse(valid_anagram("rat", "car"))
