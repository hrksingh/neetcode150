from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # 1. Add new element to the back (Standard Queue op)
        self.q.append(x)

        # 2. Rotate n-1 elements to the back
        # This moves the new element (x) to the FRONT.
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # The 'top' of our stack is now at the front of the queue
        return self.q.popleft()

    def top(self) -> int:
        # Peek at the front
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
