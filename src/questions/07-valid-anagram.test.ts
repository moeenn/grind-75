import test from "node:test"
import assert from "node:assert/strict"
import { validAnagram } from "./07-valid-anagram.ts"

test("valid anagram", () => {
    const testCases = [
        { a: "anagram", b: "nagaram", expected: true },
        { a: "rat", b: "car", expected: false },
    ]

    for (const tc of testCases) {
        const got = validAnagram(tc.a, tc.b)
        assert.equal(got, tc.expected)
    }
})
