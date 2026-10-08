from ds.binary_tree import BinaryTree, Node


def invert_node[T](node: Node[T]) -> None:
    node.left, node.right = node.right, node.left


def invert_binary_tree[T](tree: BinaryTree[T]) -> None: ...
