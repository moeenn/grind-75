from unittest import TestCase

from .queue_using_stacks import Queue


class TestQueue(TestCase):
    def test_operations(self) -> None:
        q = Queue[int]()
        q.push(1)
        q.push(2)
        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.pop())
        self.assertFalse(q.is_empty())
