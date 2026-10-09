from unittest import TestCase

from .stack import Stack


class TestStack(TestCase):
    def test_push_pop(self) -> None:
        s = Stack[int]()
        for i in range(1, 6):
            s.push(i)

        self.assertEqual(len(s), 5)
        for i in range(5, 0, -1):
            self.assertEqual(s.pop(), i)

        self.assertEqual(len(s), 0)

    def test_peek(self) -> None:
        s = Stack[int]()
        self.assertIsNone(s.peek())

        s.push(10)
        self.assertEqual(len(s), 1)
        self.assertEqual(s.peek(), 10)
        self.assertEqual(s.peek(), 10)
