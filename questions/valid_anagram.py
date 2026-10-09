def count_chars(input: str) -> dict[str, int]:
    count: dict[str, int] = {}
    for c in input:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    return count


# we could have counted chars for two string as well, and then compared the
# counts for both strings. But this would have required an extra loop.
def valid_anagram(one: str, two: str) -> bool:
    one_count = count_chars(one)
    for c in two:
        if c not in one_count:
            return False
        else:
            one_count[c] -= 1
            if one_count[c] == 0:
                del one_count[c]

    return len(one_count) == 0
