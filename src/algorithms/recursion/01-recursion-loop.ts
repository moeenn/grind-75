export function* loop<T>(data: T[]): Generator<T> {
    const [head, ...tail] = data
    if (head) yield head
    else return
    yield* loop(tail) // yield from the inner generator.
}
