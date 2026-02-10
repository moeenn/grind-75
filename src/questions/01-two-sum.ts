import assert from "node:assert"

export type Pair = {
    a: number
    b: number
}

export function twoSum(nums: number[], target: number): Pair[] {
    const max = nums.length
    assert(max > 1)

    let a = 0
    let b = 1
    let sum: number
    const result: Pair[] = []

    while (a != max - 1) {
        sum = nums[a]! + nums[b]!
        if (sum == target) {
            result.push({ a, b })
        }

        b++
        if (b == max) {
            a++
            b = a + 1
        }
    }

    return result
}
