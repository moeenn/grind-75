from unittest import TestCase

from .flood_fill import flood_fill


class TestFloodFill(TestCase):
    def test_square(self) -> None:
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        actual = flood_fill(image, 1, 1, color=2)
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertEqual(expected, actual)

    def test_rect(self) -> None:
        image = [[0, 0, 0], [0, 0, 0]]
        actual = flood_fill(image, 0, 0, color=0)
        expected = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(expected, actual)
