from unittest import TestCase

from .binary_tree import BinaryTree, Node, TraversalMethod


class TestBinaryTree(TestCase):
    r"""
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
    """

    def __build_tree(self) -> BinaryTree[int]:
        tree = BinaryTree[int]()
        tree.root = Node(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        tree.root.right.left = Node(6)
        tree.root.right.right = Node(7)
        return tree

    def test_traveral_in_order(self) -> None:
        tree = self.__build_tree()
        traversed = list(tree.traverse(TraversalMethod.IN_ORDER))
        expected = [4, 2, 5, 1, 6, 3, 7]
        self.assertEqual(expected, traversed)

    def test_traversal_pre_order(self) -> None:
        tree = self.__build_tree()
        traversed = list(tree.traverse(TraversalMethod.PRE_ORDER))
        expected = [1, 2, 4, 5, 3, 6, 7]
        self.assertEqual(expected, traversed)

    def test_traversal_post_order(self) -> None:
        tree = self.__build_tree()
        traversed = list(tree.traverse(TraversalMethod.POST_ORDER))
        expected = [4, 5, 2, 6, 7, 3, 1]
        self.assertEqual(expected, traversed)
