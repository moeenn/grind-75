import test from "node:test"
import assert from "node:assert/strict"
import { loop } from "./01-recursion-loop.ts"

test("recursion loop", () => {
    const data = [1, 2, 3, 4, 5, 6, 7, 8]
    const got = loop(data).toArray()
    assert.deepEqual(data, got)
})
