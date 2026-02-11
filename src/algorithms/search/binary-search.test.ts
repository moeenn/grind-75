import test from "node:test"
import assert from "node:assert/strict"
import { binarySearch } from "./binary-search.ts"

test("binary search", () => {
    const testCases = [
        {
            input: [1, 2, 3, 4, 5],
            targte: 3,
            expected: 2,
        },
        {
            input: [10, 20, 30, 40, 50, 60],
            targte: 50,
            expected: 4,
        },
        {
            input: [6, 7, 8, 9, 100],
            targte: 6,
            expected: 0,
        },
        {
            input: [4, 5, 6, 7, 8],
            targte: 3,
            expected: undefined,
        },
        {
            input: [20, 30, 40, 50],
            targte: 100,
            expected: undefined,
        },
    ]

    for (const tc of testCases) {
        const got = binarySearch(tc.input, tc.targte)
        assert.equal(tc.expected, got)
    }
})
