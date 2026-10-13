def can_construct(ransom_note: str, magazine: str) -> bool:
    mag_freq: dict[str, int] = {}
    for c in magazine:
        if c in mag_freq:
            mag_freq[c] += 1
        else:
            mag_freq[c] = 1

    for c in ransom_note:
        if c in mag_freq and mag_freq[c] > 0:
            mag_freq[c] -= 1
        else:
            return False

    return True
