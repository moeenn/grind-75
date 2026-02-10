import test from "node:test"
import { LinkedList } from "./LinkedList.ts"
import assert from "node:assert/strict"

test("LinkedList", () => {
    const list = new LinkedList<number>()
    assert.equal(list.length, 0)

    for (let i = 10; i <= 100; i += 10) {
        list.append(i)
    }
    assert.equal(list.length, 10)

    for (let i = 1; i <= 10; i++) {
        list.prepend(i)
    }
    assert.equal(list.length, 20)

    assert.equal(list.at(0), 10)
    assert.equal(list.at(19), 100)

    const expectedElements = [
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
    ]

    const allElements = list.iter().toArray()
    assert.deepEqual(expectedElements, allElements)

    assert(list.remove(0))
    assert(list.remove(1))
    assert.equal(18, list.length)
    assert.equal(9, list.at(0))
    assert.equal(7, list.at(1))

    for (let i = 0; i < 18; i++) {
        list.remove(0)
    }
    assert.equal(0, list.length)
    assert.deepEqual([], list.iter().toArray())
})
