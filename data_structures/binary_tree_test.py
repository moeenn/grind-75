from unittest import TestCase

from .binary_tree import BinaryTree, Node, TraversalMethod


class TestBinaryTree(TestCase):
    def __build_tree(self) -> BinaryTree[int]:
        r"""
                    1
                  /   \
                 2     3
                / \   / \
               4   5 6   7
        """

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

    def test_height_empty(self) -> None:
        tree = BinaryTree[int]()
        self.assertEqual(-1, tree.height())

    def test_height_simple(self) -> None:
        tree = self.__build_tree()
        actual = tree.height()
        expected = 2
        self.assertEqual(expected, actual)

    def test_height_long(self) -> None:
        r"""
                    1
                  /   \
                 2     3
                /
               4
              /
             5
            /
           6
        """

        tree = BinaryTree[int]()
        tree.root = Node(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.left.left = Node(5)
        tree.root.left.left.left.left = Node(6)

        expected = 4
        actual = tree.height()
        self.assertEqual(expected, actual)
