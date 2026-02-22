export function binarySearch(input: number[], target: number): number {
    const size = input.length
    let low = 0
    let high = size - 1
    let mid: number

    while (low < high) {
        mid = Math.floor((low + high) / 2)

        if (input[mid] == target) {
            return mid
        }

        if (input[mid]! < target) {
            low = mid + 1
        }

        if (input[mid]! > target) {
            high = mid
        }
    }

    return -1
}
