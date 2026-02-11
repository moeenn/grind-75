import assert from "node:assert"

export function binarySearch<T>(data: T[], target: T): option<number> {
    assert(data.length > 1)
    let start = 0
    let end = data.length - 1
    let mid = Math.floor((start + end) / 2)

    while (start < end) {
        if (target == data[mid]) {
            return mid
        }

        if (target > data[mid]!) {
            start = mid + 1
            mid = Math.floor((start + end) / 2)
        } else {
            end = mid
            mid = Math.floor((start + end) / 2)
        }
    }

    return
}
