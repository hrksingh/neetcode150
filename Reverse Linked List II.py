from typing import Optional
from dataclasses import dataclass


# Definition for singly-linked list.
@dataclass
class ListNode:
    # Declare fields here; @dataclass writes the __init__ for you!
    val: int = 0
    next: Optional["ListNode"] = None

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


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """Reverse the sublist from position `left` to `right` (1-based).

        Returns the head of the modified list.
        """
        if head is None or left == right:
            return head

        dummy = ListNode(0, head)

        # prev will point to node immediately before the sublist to reverse
        prev: ListNode = dummy
        for _ in range(left - 1):
            # prev will move to the node just before the `left` position
            prev = prev.next  # type: ignore[assignment]

        # start is the first node of the sublist to reverse (guaranteed non-None)
        start: ListNode = prev.next  # type: ignore[assignment]
        then = start.next

        # reverse the sublist by standard head-insertion method
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    res = Solution().reverseBetween(head, 2, 4)
    print(linked_list_to_list(res))
