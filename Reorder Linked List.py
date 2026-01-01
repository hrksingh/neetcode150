from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next: Optional["ListNode"] = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"

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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Reorder list in-place to: L0→Ln→L1→Ln-1→L2→..."""

        if head is None or head.next is None:
            return

        # find middle, split into two lists
        mid = self._find_mid(head)
        second = mid.next
        mid.next = None  # break first half

        # reverse second half and merge alternatingly
        second_rev = self._reverse(second)
        self._merge_alternate(head, second_rev)

    def _find_mid(self, head: ListNode) -> ListNode:
        """Return the first half's tail (middle) for splitting the list."""
        slow: ListNode = head
        fast: ListNode = head
        # advance fast two steps and slow one step until fast reaches end
        while fast.next and fast.next.next:
            slow = slow.next  # type: ignore[assignment]
            fast = fast.next.next
        return slow

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse linked list and return new head."""
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def _merge_alternate(self, a: Optional[ListNode], b: Optional[ListNode]) -> None:
        """Merge list `b` into `a` alternating nodes. Modifies `a` in-place."""
        p1, p2 = a, b
        while p1 and p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2


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
    examples = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3],
        [1],
    ]
    s = Solution()
    for arr in examples:
        head = build_linked_list(arr)
        s.reorderList(head)
        print(arr, "->", linked_list_to_list(head))
