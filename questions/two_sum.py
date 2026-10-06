from dataclasses import dataclass


@dataclass(frozen=True)
class Pair:
    first: int
    second: int


def two_sum(nums: list[int], target: int) -> list[Pair]:
    result: list[Pair] = []
    size = len(nums)
    assert size > 1

    for a in range(size - 1):
        for b in range(a + 1, size):
            sum = nums[a] + nums[b]
            if sum == target:
                result.append(Pair(a, b))

    return result
