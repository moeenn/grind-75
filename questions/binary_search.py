# note: the array should already be sorted in ascending order.
def binary_search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            end = mid
        else:
            start = mid + 1

    return -1
