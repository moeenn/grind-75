import { TreeNode } from "#src/data-structures/BinaryTree.ts"

export function invertBinaryTree<T>(node: option<TreeNode<T>>) {
    if (!node) return
    const tmp = node.left
    node.left = node.right
    node.right = tmp

    invertBinaryTree(node.left)
    invertBinaryTree(node.right)
}
