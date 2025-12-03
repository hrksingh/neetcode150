from typing import List
from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Smallest length of a contiguous subarray with sum >= target. O(n) time."""
        if not nums:
            return 0

        left = 0
        total = 0
        best = inf

        for right, val in enumerate(nums):
            total += val
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if best is inf else best


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # expect 2 (subarray [4,3])
