class MyQueue:
    def __init__(self):
        self.inn = []  # Input stack
        self.out = []  # Output stack

    def push(self, x: int) -> None:
        # O(1): Always push to input stack
        self.inn.append(x)

    def pop(self) -> int:
        # Ensure out stack has elements, then pop
        self.peek()
        return self.out.pop()

    def peek(self) -> int:
        # If out stack is empty, move everything from inn -> out
        if not self.out:
            while self.inn:
                self.out.append(self.inn.pop())
        return self.out[-1]

    def empty(self) -> bool:
        return not self.inn and not self.out
