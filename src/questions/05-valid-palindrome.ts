import assert from "node:assert"

export function isAlphanumeric(input: string, index: number): boolean {
    assert(index >= 0 && index < input.length)
    const code = input.charCodeAt(index)
    return (
        (code > 47 && code < 58) || // 0-9
        (code > 64 && code < 91) || // A-Z
        (code > 96 && code < 123) // a-z
    )
}

export function isPalindrome(input: string): boolean {
    let startIdx = 0
    let endIdx = input.length - 1

    if (startIdx == endIdx) {
        return true
    }

    while (startIdx < endIdx) {
        if (!isAlphanumeric(input, startIdx)) {
            startIdx++
        }

        if (!isAlphanumeric(input, endIdx)) {
            endIdx--
        }

        if (isAlphanumeric(input, startIdx) && isAlphanumeric(input, endIdx)) {
            if (input[startIdx]?.toLowerCase() == input[endIdx]?.toLowerCase()) {
                startIdx++
                endIdx--
            } else {
                return false
            }
        }
    }

    return true
}
