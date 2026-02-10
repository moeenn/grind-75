import test from "node:test"
import assert from "node:assert/strict"
import { validParenthesis } from "./02-valid-parentheses.ts"

test("validParenthesis", () => {
    const testCases = [
        {
            input: "()",
            expected: true,
        },
        {
            input: "()[]{}",
            expected: true,
        },
        {
            input: "(]",
            expected: false,
        },
        {
            input: "([])",
            expected: true,
        },
        {
            input: "([)]",
            expected: false,
        },
    ]

    for (const t of testCases) {
        const got = validParenthesis(t.input)
        assert.equal(got, t.expected)
    }
})
