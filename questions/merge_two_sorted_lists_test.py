from unittest import TestCase

from data_structures.linked_list import LinkedList

from .merge_two_sorted_lists import (
    merge_sorted_linked_lists,
    merge_sorted_lists,
    merge_sorted_lists_simple,
)


class TestMergeTwoSortedLinkedLists(TestCase):
    def test_scenarios(self) -> None:
        one = LinkedList[int]()
        for i in [1, 2, 4]:
            one.append(i)

        two = LinkedList[int]()
        for i in [1, 3, 4]:
            two.append(i)

        merged = merge_sorted_linked_lists(one, two)
        expected = [1, 1, 2, 3, 4, 4]
        self.assertEqual(list(merged), expected)

    def test_both_empty(self) -> None:
        one = LinkedList[int]()
        two = LinkedList[int]()

        merged = merge_sorted_linked_lists(one, two)
        self.assertEqual(list(merged), [])

    def test_one_empty(self) -> None:
        one = LinkedList[int]()
        two = LinkedList[int]()
        two.append(0)

        merged = merge_sorted_linked_lists(one, two)
        self.assertEqual(list(merged), [0])


class TestMergeTwoSortedLists(TestCase):
    def test_scenarios(self) -> None:
        one = [1, 2, 4]
        two = [1, 3, 4]
        merged = merge_sorted_lists(one, two)
        expected = [1, 1, 2, 3, 4, 4]
        self.assertEqual(merged, expected)

    def test_both_empty(self) -> None:
        one = []
        two = []
        merged = merge_sorted_lists(one, two)
        self.assertEqual(merged, [])

    def test_one_empty(self) -> None:
        one = []
        two = [0]
        merged = merge_sorted_lists(one, two)
        self.assertEqual(merged, [0])


class TestMergeTwoSortedListsSimple(TestCase):
    def test_scenarios(self) -> None:
        one = [1, 2, 4]
        two = [1, 3, 4]
        merged = merge_sorted_lists_simple(one, two)
        expected = [1, 1, 2, 3, 4, 4]
        self.assertEqual(merged, expected)

    def test_both_empty(self) -> None:
        one = []
        two = []
        merged = merge_sorted_lists_simple(one, two)
        self.assertEqual(merged, [])

    def test_one_empty(self) -> None:
        one = []
        two = [0]
        merged = merge_sorted_lists_simple(one, two)
        self.assertEqual(merged, [0])
