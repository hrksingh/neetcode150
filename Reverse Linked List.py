from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Reverse the connection between current and next
        head.next.next = head  # Next node points back to current
        head.next = None  # Current node points to None

        return new_head


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
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    # Linked list = 1 -> 2 -> 3
    head = build_linked_list([1, 2, 3])
    new_head = Solution().reverseList(head)
    print(linked_list_to_list(new_head))
