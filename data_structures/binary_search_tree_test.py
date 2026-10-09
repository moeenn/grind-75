from unittest import TestCase

from .binary_search_tree import BinarySearchTree, TraversalMethod


class TestBinarySearchTree(TestCase):
    def test_insertion_simple(self) -> None:
        tree = BinarySearchTree[int]()
        tree.insert(10)
        tree.insert(15)
        tree.insert(5)
        self.assertEqual(len(tree), 3)

        expected = [5, 10, 15]
        actual = list(tree.traverse(TraversalMethod.IN_ORDER))
        self.assertEqual(expected, actual)

    def test_insertion_deep(self) -> None:
        r"""
                 10
               /   \
              5     15
             / \   /  \
            3   7 12   16

        """
        tree = BinarySearchTree[int]()
        self.assertTrue(tree.insert(10))
        self.assertTrue(tree.insert(5))
        self.assertTrue(tree.insert(15))
        self.assertTrue(tree.insert(16))
        self.assertTrue(tree.insert(3))
        self.assertTrue(tree.insert(12))
        self.assertTrue(tree.insert(7))
        self.assertFalse(tree.insert(7))
        self.assertFalse(tree.insert(7))
        self.assertEqual(len(tree), 7)

        expected = [3, 5, 7, 10, 12, 15, 16]
        actual = list(tree.traverse(TraversalMethod.IN_ORDER))
        self.assertEqual(expected, actual)

    def test_find_valid(self) -> None:
        tree = BinarySearchTree[int]()
        self.assertTrue(tree.insert(10))
        self.assertTrue(tree.insert(5))
        self.assertTrue(tree.insert(15))
        self.assertIsNotNone(tree.find(5))

    def test_find_invalid(self) -> None:
        tree = BinarySearchTree[int]()
        self.assertTrue(tree.insert(10))
        self.assertTrue(tree.insert(5))
        self.assertTrue(tree.insert(15))
        self.assertIsNone(tree.find(50))
