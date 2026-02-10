import test from "node:test"
import { isAlphanumeric, isPalindrome } from "./05-valid-palindrome.ts"
import assert from "node:assert/strict"

test("isAlphanumeric", () => {
    const testCases = [
        { input: "0", expected: true },
        { input: "9", expected: true },
        { input: "A", expected: true },
        { input: "Z", expected: true },
        { input: "a", expected: true },
        { input: "z", expected: true },
        { input: " ", expected: false },
        { input: ",", expected: false },
        { input: ":", expected: false },
    ]

    for (const tc of testCases) {
        const got = isAlphanumeric(tc.input, 0)
        assert.equal(got, tc.expected)
    }
})

test("valid palindrom", () => {
    const testCases = [
        { input: "A man, a plan, a canal: Panama", expected: true },
        { input: "race a car", expected: false },
        { input: " ", expected: true },
    ]

    for (const testCase of testCases) {
        const got = isPalindrome(testCase.input)
        assert.equal(got, testCase.expected)
    }
})
