from collections.abc import Generator
from dataclasses import dataclass
from typing import Self


@dataclass
class Node[T]:
    data: T
    next: Self | None = None
    prev: Self | None = None


class DoublyLinkedList[T]:
    head: Node[T] | None
    tail: Node[T] | None
    size: int

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def append(self, data: T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        new_node.prev = current
        current.next = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, data: T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        tmp = self.head
        tmp.prev = new_node
        new_node.next = tmp
        self.head = new_node
        self.size += 1

    def __iter__(self) -> Generator[T]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def reverse(self) -> None:
        current = self.head
        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        self.head, self.tail = self.tail, self.head
