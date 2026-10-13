# n is majority if it appears more than size/2 time.
def majority_element(nums: list[int]) -> int | None:
    freq: dict[int, int] = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    majority = len(nums) / 2
    for n, count in freq.items():
        if count >= majority:
            return n
