class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next: "ListNode | None" = None

    def __repr__(self):
        return f"ListNode(key={self.key},next={self.next})"


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

    def __str__(self):
        result = []
        for bucket in self.set:
            cur = bucket.next
            while cur:
                result.append(cur.key)
                cur = cur.next
        return str(result)

    def printHashSet(self):
        print(self.set)


h = MyHashSet()
h.add(7)
h.add(10007)
h.add(17)
h.add(2)
h.add(43)
h.add(718)
print(h.contains(718))
print("------")
h.printHashSet()
h.remove(718)
print(h.contains(718))
print("------")
h.printHashSet()
