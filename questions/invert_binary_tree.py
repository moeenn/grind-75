from ds.binary_tree import BinaryTree, Node


def invert_binary_tree[T](tree: BinaryTree[T]) -> None:
    def invert(node: Node[T] | None) -> None:
        if node is None:
            return

        node.left, node.right = node.right, node.left
        invert(node.left)
        invert(node.right)

    invert(tree.root)
