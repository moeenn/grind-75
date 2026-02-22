export class TreeNode<T> {
    data: T
    left: option<TreeNode<T>> = undefined
    right: option<TreeNode<T>> = undefined

    constructor(data: T) {
        this.data = data
    }

    setLeft(left: option<TreeNode<T>>) {
        this.left = left
    }

    setRight(right: option<TreeNode<T>>) {
        this.right = right
    }
}

export class BinaryTree<T> {
    root: option<TreeNode<T>> = undefined

    // current -> left -> right.
    static *traversePreOrder<T>(node: option<TreeNode<T>>): Generator<T> {
        if (!node) return
        yield node.data
        yield* BinaryTree.traversePreOrder(node.left)
        yield* BinaryTree.traversePreOrder(node.right)
    }

    // left -> current -> right.
    static *traverseInOrder<T>(node: option<TreeNode<T>>): Generator<T> {
        if (!node) return
        yield* BinaryTree.traverseInOrder(node.left)
        yield node.data
        yield* BinaryTree.traverseInOrder(node.right)
    }

    // left -> right -> current.
    static *traversePostOrder<T>(node: option<TreeNode<T>>): Generator<T> {
        if (!node) return
        yield* BinaryTree.traversePostOrder(node.left)
        yield* BinaryTree.traversePostOrder(node.right)
        yield node.data
    }
}
