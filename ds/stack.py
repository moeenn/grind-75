class Stack[T]:
    data: list[T]

    def __init__(self) -> None:
        self.data = []

    def __len__(self) -> int:
        return len(self.data)

    def push(self, data: T) -> None:
        self.data.append(data)

    def pop(self) -> T | None:
        return self.data.pop()

    def peek(self) -> T | None:
        if len(self.data) == 0:
            return None
        return self.data[-1]
