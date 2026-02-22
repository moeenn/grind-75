import test from "node:test"
import assert from "node:assert/strict"
import { BinaryTree, TreeNode } from "./BinaryTree.ts"

//                 1
//               /   \
//             2      3
//           /  \    / \
//          4    5  6   7

test("binary tree", () => {
    const tree = new BinaryTree<number>()
    tree.root = new TreeNode(1)

    const two = new TreeNode(2)
    const three = new TreeNode(3)
    tree.root.setLeft(two)
    tree.root.setRight(three)

    two.setLeft(new TreeNode(4))
    two.setRight(new TreeNode(5))

    three.setLeft(new TreeNode(6))
    three.setRight(new TreeNode(7))

    const preorder = BinaryTree.traversePreOrder(tree.root).toArray()
    assert.deepEqual(preorder, [1,2,4,5,3,6,7])

    const inorder = BinaryTree.traverseInOrder(tree.root).toArray()
    assert.deepEqual(inorder, [4,2,5,1,6,3,7])

    const postorder = BinaryTree.traversePostOrder(tree.root).toArray()
    assert.deepEqual(postorder, [4,5,2,6,7,3,1])
})
