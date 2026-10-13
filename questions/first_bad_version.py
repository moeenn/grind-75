from collections.abc import Callable

IsBadVersion = Callable[[int], bool]


def first_bad_version(n: int, is_bad_version: IsBadVersion) -> int:
    start = 1
    end = n

    while start < end:
        mid = (start + end) // 2
        if is_bad_version(mid):
            end = mid
        else:
            start = mid + 1

    return start
