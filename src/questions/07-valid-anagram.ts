type Charset = Map<string, number>

function getCharset(input: string): Charset {
    const result = new Map<string, number>()
    for (const c of input) {
        const found = result.get(c)
        if (!found) {
            result.set(c, 1)
        } else {
            result.set(c, found + 1)
        }
    }

    return result
}

function matchCharset(a: Charset, b: Charset): boolean {
    if (a.size != b.size) return false
    for (const [k, v] of a.entries()) {
        const found = b.get(k)
        if (v != found) return false
    }

    return true
}

export function validAnagram(a: string, b: string): boolean {
    const aCharset = getCharset(a)
    const bCharset = getCharset(b)
    return matchCharset(aCharset, bCharset)
}
