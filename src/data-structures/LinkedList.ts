import assert from "node:assert"

class Node<T> {
    data: T
    next: option<Node<T>>

    constructor(data: T, next: option<Node<T>> = undefined) {
        this.data = data
        this.next = next
    }

    setNext(next: Node<T>) {
        this.next = next
    }
}

export class LinkedList<T> {
    #head: option<Node<T>>
    #length: number

    constructor() {
        this.#head = undefined
        this.#length = 0
    }

    append(data: T) {
        const newNode = new Node<T>(data)
        if (!this.#head) {
            this.#head = newNode
            this.#length++
            return
        }

        let current: option<Node<T>> = this.#head
        for (; current?.next != null; current = current.next) {}
        current.setNext(newNode)
        this.#length++
    }

    prepend(data: T) {
        const newNode = new Node(data)
        if (!this.#head) {
            this.#head = newNode
            this.#length++
            return
        }

        newNode.setNext(this.#head)
        this.#head = newNode
        this.#length++
    }

    at(index: number): option<T> {
        assert(index >= 0)
        if (index >= this.#length) return undefined
        let current = this.#head
        let i = 0

        for (; current != null; current = current.next) {
            if (i == index) {
                return current.data
            }
            i++
        }

        return undefined
    }

    remove(index: number): boolean {
        assert(index >= 0)
        if (index >= this.#length) return false

        let current = this.#head
        let prev: option<Node<T>>
        let i = 0

        while (current != undefined) {
            if (i == index) {
                if (prev) {
                    prev.next = current.next
                } else {
                    this.#head = this.#head?.next
                }
                this.#length--
                return true
            }

            prev = current
            current = current.next
            i++
        }

        return false
    }

    *iter(): Generator<T> {
        let current = this.#head
        for (; current != null; current = current.next) {
            yield current.data
        }
    }

    get length(): number {
        return this.#length
    }
}
