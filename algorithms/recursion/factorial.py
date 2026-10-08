def factorial(n: int) -> int:
    def loop(accum: int, n: int) -> int:
        if n <= 1:
            return accum
        return loop(n * accum, n - 1)

    return loop(1, n)
