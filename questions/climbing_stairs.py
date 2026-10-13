# This is the same formula for calculating fibonacci sequence.
# 1 2 3 5 8 13 ...
def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)
