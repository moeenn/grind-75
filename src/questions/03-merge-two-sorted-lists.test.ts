import { LinkedList } from "#src/data-structures/LinkedList.ts"
import test from "node:test"
import { mergeTwoSortedLists } from "./03-merge-two-sorted-lists.ts"
import assert from "assert"

test("mergeTwoSortedLists", (t) => {
    t.test("basic scenario", () => {
        const a = new LinkedList<number>()
        {
            a.append(1)
            a.append(2)
            a.append(4)
        }

        const b = new LinkedList<number>()
        {
            b.append(1)
            b.append(3)
            b.append(4)
        }

        const merged = mergeTwoSortedLists(a, b)
        const expected = [1, 1, 2, 3, 4, 4]
        const got = merged.iter().toArray()
        assert.deepEqual(expected, got)
    })

    t.test("empty lists", () => {
        const a = new LinkedList<number>()
        const b = new LinkedList<number>()
        const merged = mergeTwoSortedLists(a, b)
        assert.deepEqual([], merged.iter().toArray())
    })

    t.test("one empty list", () => {
        const a = new LinkedList<number>()
        const b = new LinkedList<number>()
        b.append(0)

        const merged = mergeTwoSortedLists(a, b)
        assert.deepEqual([0], merged.iter().toArray())
    })
})
