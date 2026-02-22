import test from "node:test"
import assert from "node:assert/strict"
import { binarySearch } from "./08-binary-search.ts"

test("binary search", () => {
    const testCases = [
        {
            input: [-1, 0, 3, 5, 9, 12],
            target: 9,
            expected: 4,
        },
        {
            input: [-1, 0, 3, 5, 9, 12],
            target: 2,
            expected: -1,
        },
    ]

    for (const tc of testCases) {
        const got = binarySearch(tc.input, tc.target)
        assert.equal(got, tc.expected)
    }
})
