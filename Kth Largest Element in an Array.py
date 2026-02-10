import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                heapq.heappushpop(min_heap, n)

        return min_heap[0]

# TODO: Learn quickselect to make it more optimal
