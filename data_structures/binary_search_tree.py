from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum, auto
from typing import Self

Number = int | float


@dataclass
class Node[T: Number]:
    key: T
    left: Self | None = None
    right: Self | None = None


class TraversalMethod(Enum):
    IN_ORDER = auto()
    PRE_ORDER = auto()
    POST_ORDER = auto()


# TODO:
# - delete node.
class BinarySearchTree[T: Number]:
    root: Node | None
    size: int

    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def traverse(self, method: TraversalMethod) -> Generator[T]:
        def loop(node) -> Generator[T]:
            if node is None:
                return

            match method:
                case TraversalMethod.IN_ORDER:
                    yield from loop(node.left)
                    yield node.key
                    yield from loop(node.right)

                case TraversalMethod.PRE_ORDER:
                    yield node.key
                    yield from loop(node.left)
                    yield from loop(node.right)

                case TraversalMethod.POST_ORDER:
                    yield from loop(node.left)
                    yield from loop(node.right)
                    yield node.key

        yield from loop(self.root)

    def insert(self, key: T) -> bool:
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            self.size += 1
            return True

        current = self.root
        while True:
            if key == current.key:
                return False

            elif key < current.key:
                if current.left is None:
                    current.left = new_node
                    self.size += 1
                    return True
                else:
                    current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    self.size += 1
                    return True
                else:
                    current = current.right

    def find(self, key: int) -> Node[T] | None:
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
