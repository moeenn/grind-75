from dataclasses import dataclass
from typing import Self


@dataclass
class Node[T]:
    left: Self | None
    right: Self | None


class BinaryTree[T]:
    root: Node[T] | None
