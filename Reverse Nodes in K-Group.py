# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(-1, head)
        group_prev = dummy

        while True:
            kth_node = self.get_kth_node(group_prev, k)
            if not kth_node:
                break
            group_next = kth_node.next

            prev, cur = group_next, group_prev.next

            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp
        return dummy.next

    def get_kth_node(self, start, k):
        while start and k > 0:
            start = start.next
            k -= 1
        return start
