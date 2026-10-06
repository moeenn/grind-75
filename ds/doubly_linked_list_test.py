from unittest import TestCase

from .doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(TestCase):
    def test_append_and_size(self) -> None:
        ll = DoublyLinkedList[int]()
        for i in range(1, 11):
            ll.append(i)

        self.assertEqual(len(ll), 10)
        as_list = list(ll)
        expected = list(range(1, 11))
        self.assertEqual(as_list, expected)

    def test_prepend_and_size(self) -> None:
        ll = DoublyLinkedList[int]()
        for i in range(10, 101, 10):
            ll.prepend(i)

        self.assertEqual(len(ll), 10)
        as_list = list(ll)
        expected = list(range(100, 9, -10))
        self.assertEqual(as_list, expected)

    def test_tail(self) -> None:
        ll = DoublyLinkedList[int]()
        for i in range(1, 6):
            ll.append(i)

        self.assertEqual(len(ll), 5)
        self.assertIsNotNone(ll.head)
        self.assertEqual(ll.head.data, 1)
        self.assertIsNotNone(ll.tail)
        self.assertEqual(ll.tail.data, 5)

        ll.prepend(10)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(len(ll), 6)
        self.assertEqual(ll.tail.data, 5)

    def test_reverse(self) -> None:
        ll = DoublyLinkedList[int]()
        for i in range(1, 11):
            ll.append(i)

        self.assertEqual(list(ll), list(range(1, 11)))
        ll.reverse()
        self.assertEqual(list(ll), list(range(10, 0, -1)))
