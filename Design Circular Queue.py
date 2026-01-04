class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        self.front = ListNode(0, None, None)
        self.rear = ListNode(0, None, self.front)
        self.front.next = self.rear

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = ListNode(value, self.rear, self.rear.prev)
        self.rear.prev.next = cur
        self.rear.prev = cur
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.next = self.front.next.next
        self.front.next.prev = self.front
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.prev.val

    def isEmpty(self) -> bool:
        return self.front.next == self.rear

    def isFull(self) -> bool:
        return self.space == 0


def _queue_to_list(q: MyCircularQueue) -> list[int]:
    node = q.front.next
    out: list[int] = []
    while node is not None and node is not q.rear:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    q = MyCircularQueue(3)
    print('enQueue 1 ->', q.enQueue(1))
    print('enQueue 2 ->', q.enQueue(2))
    print('enQueue 3 ->', q.enQueue(3))
    print('enQueue 4 (should be False/full) ->', q.enQueue(4))
    print('Rear ->', q.Rear())
    print('isFull ->', q.isFull())
    print('deQueue ->', q.deQueue())
    print('enQueue 4 ->', q.enQueue(4))
    print('Rear ->', q.Rear())
    print('Front ->', q.Front())
    print('isEmpty ->', q.isEmpty())
    print('queue list ->', _queue_to_list(q))
