class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles the edge case of deleting the head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 1. Advance 'right' pointer so there is a gap of 'n' between left and right
        while n > 0 and right:
            right = right.next
            n -= 1

        # 2. Move both until 'right' hits the end
        while right:
            right = right.next
            left = left.next

        # 3. 'left' is now at the node BEFORE the one we want to delete
        left.next = left.next.next

        return dummy.next
