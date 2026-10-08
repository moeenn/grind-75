from unittest import TestCase

from ds.binary_tree import BinaryTree, Node, TraversalMethod

from .invert_binary_tree import invert_binary_tree


class TestInvertBinaryTree(TestCase):
    def test_simple(self) -> None:
        tree = BinaryTree[int]()
        tree.root = Node(4)
        tree.root.left = Node(2)
        tree.root.right = Node(7)
        tree.root.left.left = Node(1)
        tree.root.left.right = Node(3)
        tree.root.right.left = Node(6)
        tree.root.right.right = Node(9)

        expected = BinaryTree[int]()
        expected.root = Node(4)
        expected.root.left = Node(7)
        expected.root.right = Node(2)
        expected.root.left.left = Node(9)
        expected.root.left.right = Node(6)
        expected.root.right.left = Node(3)
        expected.root.right.right = Node(1)

        invert_binary_tree(tree)
        self.assertEqual(
            list(expected.traverse(TraversalMethod.IN_ORDER)),
            list(tree.traverse(TraversalMethod.IN_ORDER)),
        )
