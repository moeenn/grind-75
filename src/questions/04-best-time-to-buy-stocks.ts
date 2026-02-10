import assert from "node:assert"

export function maxProfit(prices: number[]): number {
    assert(prices.length > 1)
    let a = 0
    let b = 1
    const max = prices.length

    let profit = 0
    let maxProfile = 0

    while (a != max - 1) {
        profit = prices[b]! - prices[a]!
        if (profit > maxProfile) {
            maxProfile = profit
        }

        b++
        if (b == max) {
            a++
            b = a + 1
        }
    }

    return maxProfile
}
