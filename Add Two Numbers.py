from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        resultLL = head = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            curSum = carry

            if l1:
                curSum += l1.val
                l1 = l1.next

            if l2:
                curSum += l2.val
                l2 = l2.next

            carry = curSum // 10
            val = curSum % 10

            resultLL.next = ListNode(val)
            resultLL = resultLL.next
        return head.next


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


if __name__ == "__main__":
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    print("List 1 as list : ", linked_list_to_list(l1))
    print("List 2 as list : ", linked_list_to_list(l2))
    l3 = Solution().addTwoNumbers(l1, l2)
    print("return List  ->", linked_list_to_list(l3))
