from unittest import TestCase

from .binary_search import binary_search


class TestBinarySearch(TestCase):
    def test_found(self) -> None:
        result = binary_search([-1, 0, 3, 5, 9, 12], target=9)
        self.assertEqual(4, result)

    def test_not_found(self) -> None:
        result = binary_search([-1, 0, 3, 5, 9, 12], target=2)
        self.assertEqual(-1, result)

    def test_found_mid(self) -> None:
        result = binary_search([1, 2, 3, 4, 5, 6, 7], target=4)
        self.assertEqual(3, result)
