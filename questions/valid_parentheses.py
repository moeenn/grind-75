def is_closing(one: str, two: str) -> bool:
    return (
        one == "("
        and two == ")"
        or one == "{"
        and two == "}"
        or one == "["
        and two == "]"
    )


def valid_parentheses(input: str) -> bool:
    stack = []
    for c in input:
        match c:
            case "(" | "{" | "[":
                stack.append(c)

            case ")" | "}" | "]":
                popped = stack.pop()
                if not is_closing(popped, c):
                    return False

            case _:
                return False

    return len(stack) == 0
