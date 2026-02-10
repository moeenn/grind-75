import test from "node:test"
import { maxProfit } from "./04-best-time-to-buy-stocks.ts"
import assert from "node:assert/strict"

test("best time to buy stocks", () => {
    const testCases = [
        {
            input: [7, 1, 5, 3, 6, 4],
            expected: 5,
        },
        {
            input: [7, 6, 4, 3, 1],
            expected: 0,
        },
    ]

    for (const testCase of testCases) {
        const got = maxProfit(testCase.input)
        assert.equal(got, testCase.expected)
    }
})
