import test from "node:test"
import assert from "node:assert/strict"
import { factorial, tailOptimizedFactorial } from "./02-factorial.ts"

test("factorial", (t) => {
    t.test("basic", () => {
        const got = factorial(6)
        assert.equal(720, got)
    })

    t.test("tail optimized", () => {
        const got = tailOptimizedFactorial(6)
        assert.equal(720, got)
    })
})
