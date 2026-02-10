export class Stack<T> {
    #buffer: T[]
    #size: number
    #i = 0

    constructor(size: number) {
        this.#buffer = new Array(size)
        this.#size = size
    }

    push(item: T): boolean {
        if (this.#i == this.#size) return false
        this.#buffer[this.#i] = item
        this.#i++
        return true
    }

    pop(): option<T> {
        if (this.#i == 0) return
        this.#i--
        return this.#buffer[this.#i]
    }

    peek(): option<T> {
        if (this.#i == 0) return
        return this.#buffer[this.#i - 1]
    }

    get length(): number {
        return this.#i
    }
}
