# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"

    def __str__(self) -> str:
        vals = self.to_list(20)
        if vals and vals[-1] == "...":
            return "->".join(map(str, vals[:-1])) + "->..."
        return "->".join(map(str, vals))

    def to_list(self, limit: int = 1000) -> list[object]:
        out: list[object] = []
        node = self
        i = 0
        while node and i < limit:
            out.append(node.val)
            node = node.next
            i += 1
        if node:
            out.append("...")
        return out


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next


if __name__ == "__main__":
    a = build_linked_list([1, 2, 4])
    b = build_linked_list([1, 3, 4])
    print("List 1 as list : ", a)
    print("List 2 as list : ", b)
    merged = Solution().mergeTwoLists(a, b)
    print("merged ->", merged)
