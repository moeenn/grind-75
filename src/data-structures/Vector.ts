export class Vector<T> {
    #buffer: T[]
    #length: number
    #capacity: number

    constructor(capacity: number = 4) {
        this.#buffer = new Array<T>(capacity)
        this.#length = 0
        this.#capacity = capacity
    }

    get length(): number {
        return this.#length
    }

    *iter(): Generator<T> {
        for (let i = 0; i < this.length; i++) yield this.#buffer[i]
    }

    #shouldResize(): boolean {
        return this.#length == this.#capacity
    }

    #resize() {
        const newCapacity = this.#capacity * 2
        const newBuffer = new Array<T>(newCapacity)

        for (let i = 0; i < this.#length; i++) {
            newBuffer[i] = this.#buffer[i]
        }

        this.#capacity = newCapacity
        this.#buffer = newBuffer
    }

    push(data: T) {
        if (this.#shouldResize()) {
            this.#resize()
        }

        this.#buffer[this.#length] = data
        this.#length++
    }

    at(index: number): option<T> {
        assert(index >= 0)
        if (index >= this.#length) return
        return this.#buffer[index]
    }

    remove(index: number): boolean {
        assert(index >= 0)
        if (index >= this.#length) return false

        // TODO: find out how vectors handles element removals.
    }
}
