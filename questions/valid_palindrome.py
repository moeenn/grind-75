def valid_palindrom(input: str) -> bool:
    start = 0
    end = len(input) - 1
    input = input.lower()

    while start < end:
        if not input[start].isalnum():
            start += 1
            continue

        if not input[end].isalnum():
            end -= 1
            continue

        if input[start] == input[end]:
            start += 1
            end -= 1
        else:
            return False

    return True
