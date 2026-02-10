import { Stack } from "#src/data-structures/Stack.ts"

function getOpeningBracket(closingBracket: string): string {
    switch (closingBracket) {
        case ")":
            return "("

        case "}":
            return "{"

        case "]":
            return "["

        default:
            throw new Error("invalid closing bracket: " + closingBracket)
    }
}

export function validParenthesis(input: string): boolean {
    const stack = new Stack<string>(20)
    let openingBracket: string
    let peeked: string | undefined

    for (const char of input) {
        switch (char) {
            case "(":
            case "{":
            case "[":
                stack.push(char)
                break

            case ")":
            case "}":
            case "]":
                openingBracket = getOpeningBracket(char)
                peeked = stack.peek()
                if (!peeked) return false // closed without opening.
                if (openingBracket !== peeked) return false
                stack.pop()
        }
    }

    return true
}
