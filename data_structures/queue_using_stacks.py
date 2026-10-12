class Queue[T]:
    in_stack: list[T]
    out_stack: list[T]
    size: int

    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []
        self.size = 0

    def push(self, data: T) -> None:
        self.in_stack.append(data)
        self.size += 1

    # copy from in_stack onto out_stack, whereby reversing their order.
    def __transfer(self) -> None:
        if len(self.in_stack) == 0:
            return

        while len(self.in_stack) != 0:
            item = self.in_stack.pop()
            self.out_stack.append(item)

    def pop(self) -> T | None:
        self.__transfer()
        return self.out_stack.pop()

    def peek(self) -> T | None:
        self.__transfer()
        return self.out_stack[len(self.out_stack) - 1]

    def is_empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
