import test from "node:test"
import assert from "node:assert/strict"
import { invertBinaryTree } from "./06-invert-binary-tree.ts"
import { BinaryTree, TreeNode } from "#src/data-structures/BinaryTree.ts"

test("invert binary tree", (t) => {
    t.test("basic tree", () => {
        const tree = new BinaryTree()
        tree.root = new TreeNode(2)

        const c1 = new TreeNode(1)
        const c2 = new TreeNode(3)
        tree.root.setLeft(c1)
        tree.root.setRight(c2)

        const expected = [3, 2, 1]
        invertBinaryTree(tree.root)
        const got = BinaryTree.traverseInOrder(tree.root).toArray()
        assert.deepEqual(got, expected)
    })

    t.test("larger tree", () => {
        const tree = new BinaryTree()
        tree.root = new TreeNode(4)

        const c1 = new TreeNode(2)
        const c2 = new TreeNode(7)
        tree.root.setLeft(c1)
        tree.root.setRight(c2)

        c1.setLeft(new TreeNode(1))
        c1.setRight(new TreeNode(3))

        c2.setLeft(new TreeNode(6))
        c2.setRight(new TreeNode(9))

        const expected = [9, 7, 6, 4, 3, 2, 1]
        invertBinaryTree(tree.root)
        const got = BinaryTree.traverseInOrder(tree.root).toArray()
        assert.deepEqual(got, expected)
    })
})
