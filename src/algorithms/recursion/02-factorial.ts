export function factorial(n: number): number {
    if (n == 0) return 1
    return n * factorial(n - 1)
}

export function tailOptimizedFactorial(n: number, product = 1): number {
    if (n == 0) return product
    return tailOptimizedFactorial(n - 1, product * n)
}
