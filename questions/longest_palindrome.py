def longest_palindrome(input: str) -> int:
    freq: dict[str, int] = {}
    for c in input:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    result = 0
    odd = False
    for c, count in freq.items():
        if count % 2 == 0:
            result += count
        else:
            odd = True

    return result + 1 if odd else result
