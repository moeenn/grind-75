import test from "node:test"
import { Stack } from "./Stack.ts"
import assert from "node:assert/strict"

test("stack", () => {
    const s = new Stack(4)
    assert(s.push(10))
    assert(s.push(20))
    assert(s.push(30))
    assert(s.push(40))
    assert.equal(s.push(50), false)
    assert.equal(s.length, 4)

    assert.equal(s.pop(), 40)
    assert.equal(s.pop(), 30)
    assert.equal(s.pop(), 20)
    assert.equal(s.length, 1)

    assert.equal(s.peek(), 10)
    assert.equal(s.length, 1)

    assert.equal(s.pop(), 10)
    assert.equal(s.pop(), undefined)
})
