export function* loop<T>([head, ...tail]: T[]): Generator<T> {
    if (head) yield head
    else return
    yield* loop(tail) // yield from the inner generator.
}
