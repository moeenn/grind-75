import test from "node:test"
import assert from "node:assert/strict"
import { bubbleSort } from "./bubble-sort.ts"

test("bubble sort", () => {
    const testCases = [
        {
            input: [100, 90, 80, 70, 60, 50, 40],
            expected: [40, 50, 60, 70, 80, 90, 100],
        },
        {
            input: [-2, 45, 0, 11, -9],
            expected: [-9, -2, 0, 11, 45],
        },
    ]

    for (const tc of testCases) {
        bubbleSort(tc.input)
        assert.deepEqual(tc.input, tc.expected)
    }
})
