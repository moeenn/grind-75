from collections.abc import Generator
from dataclasses import dataclass
from typing import Self


@dataclass
class Node[T]:
    data: T
    next: Self | None = None


class LinkedList[T]:
    head: Node[T] | None
    size: int

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def append(self, data: T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.size += 1

    def prepend(self, data: T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        tmp = self.head
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
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
