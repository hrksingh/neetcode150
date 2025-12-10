from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Stores INDICES
        l = 0  # Left pointer of the window

        for r in range(len(nums)):
            # 1. Clean Front: Remove index if it's outside the new window [l, r]
            if q and q[0] < l:
                q.popleft()

            # 2. Clean Back: Maintain decreasing order
            # Remove smaller elements because they are now "useless"
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # 3. Add current element
            q.append(r)

            # 4. Record Result: Once window hits size k
            if r - l + 1 == k:
                res.append(nums[q[0]])  # Front is always the max
                l += 1  # Slide the window forward

        return res
