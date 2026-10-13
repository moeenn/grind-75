from unittest import TestCase

from .ranson_note import can_construct


class TestRansomNoteConstruct(TestCase):
    def test_can_construct(self) -> None:
        cases = [
            ("a", "b", False),
            ("aa", "ab", False),
            ("aa", "aab", True),
        ]

        for ransom_note, magazine, expected in cases:
            self.assertEqual(expected, can_construct(ransom_note, magazine))
