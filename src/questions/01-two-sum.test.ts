import test from "node:test"
import assert from "node:assert/strict"
import { twoSum } from "./01-two-sum.ts"

test("two sum", () => {
    const testCases = [
        {
            input: [2, 7, 11, 15],
            target: 9,
            expected: [{ a: 0, b: 1 }],
        },
        {
            input: [3, 2, 4],
            target: 6,
            expected: [{ a: 1, b: 2 }],
        },
        {
            input: [3, 3],
            target: 6,
            expected: [{ a: 0, b: 1 }],
        },
    ]

    for (const tc of testCases) {
        const got = twoSum(tc.input, tc.target)
        assert.deepEqual(got, tc.expected)
    }
})
