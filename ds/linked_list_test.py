from unittest import TestCase

from .linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_append_and_size(self) -> None:
        ll = LinkedList[int]()
        for i in range(1, 11):
            ll.append(i)

        self.assertEqual(len(ll), 10)
        as_list = ll.to_list()
        self.assertEqual(as_list, list(range(1, 11)))

    def test_prepend_and_size(self) -> None:
        ll = LinkedList[int]()
        for i in range(10, 101, 10):
            ll.prepend(i)

        expected = list(range(100, 9, -10))
        self.assertEqual(ll.to_list(), expected)
