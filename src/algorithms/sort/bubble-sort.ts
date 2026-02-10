import assert from "node:assert"

function swap(data: number[], a: number, b: number) {
    assert(a != b)
    let tmp = data[a]
    data[a] = data[b]
    data[b] = tmp
}

export function bubbleSort(input: number[]): void {
    assert(input.length > 1)
    let a = 0
    let b = 1
    const max = input.length
    let iter = 0

    while (iter != max - 1) {
        if (input[a] > input[b]) {
            swap(input, a, b)
        }

        a++
        b++

        if (b == max - iter) {
            a = 0
            b = a + 1
            iter++
        }
    }
}
