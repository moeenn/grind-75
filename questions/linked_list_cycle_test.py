from unittest import TestCase

from data_structures.linked_list import LinkedList, Node

from .linked_list_cycle import has_cycle


class TestLinkedListCycle(TestCase):
    def test_has_cycle(self) -> None:
        ll = LinkedList[int]()
        repeat_node = Node(100)
        ll.head = Node(10)
        ll.head.next = Node(20)
        ll.head.next.next = repeat_node
        ll.head.next.next.next = Node(30)
        ll.head.next.next.next = Node(40)
        ll.head.next.next.next.next = repeat_node
        self.assertTrue(has_cycle(ll))

    def test_has_no_cycle(self) -> None:
        ll = LinkedList[int]()
        ll = LinkedList[int]()
        ll.head = Node(10)
        ll.head.next = Node(20)
        ll.head.next.next = Node(30)
        ll.head.next.next.next = Node(40)
        ll.head.next.next.next.next = Node(50)
        self.assertFalse(has_cycle(ll))
