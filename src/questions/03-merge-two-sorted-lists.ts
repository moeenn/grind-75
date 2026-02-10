import { LinkedList } from "#src/data-structures/LinkedList.ts"

export function mergeTwoSortedLists(
    a: LinkedList<number>,
    b: LinkedList<number>,
): LinkedList<number> {
    if (a.length == 0) return b
    if (b.length == 0) return a

    const merged = new LinkedList<number>()
    let i = 0
    let j = 0

    let first: option<number>
    let second: option<number>

    while (i < a.length && j < b.length) {
        first = a.at(i)!
        second = b.at(j)!

        if (first < second) {
            merged.append(first)
            i++
        }

        if (second < first) {
            merged.append(second)
            j++
        }

        if (first == second) {
            merged.append(first)
            merged.append(second)
            i++
            j++
        }
    }

    return merged
}
