from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum, auto
from typing import Self


@dataclass
class Node[T]:
    value: T
    left: Self | None = None
    right: Self | None = None

    def set_value(self, value: T) -> None:
        self.value = value


# depth-first-search (DFS) methods.
class TraversalMethod(Enum):
    IN_ORDER = auto()
    PRE_ORDER = auto()
    POST_ORDER = auto()


class BinaryTree[T]:
    root: Node[T] | None

    def traverse(self, method: TraversalMethod) -> Generator[T]:
        def loop(node: Node[T] | None) -> Generator[T]:
            if node is None:
                return

            match method:
                case TraversalMethod.IN_ORDER:
                    yield from loop(node.left)
                    yield node.value
                    yield from loop(node.right)

                case TraversalMethod.PRE_ORDER:
                    yield node.value
                    yield from loop(node.left)
                    yield from loop(node.right)

                case TraversalMethod.POST_ORDER:
                    yield from loop(node.left)
                    yield from loop(node.right)
                    yield node.value

        yield from loop(self.root)
