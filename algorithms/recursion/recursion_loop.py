from collections.abc import Generator


def loop[T](data: list[T]) -> Generator[T]:
    if len(data) == 0:
        return

    yield data[0]
    yield from loop(data[1:])
