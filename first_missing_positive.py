from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Return the smallest missing positive integer.
        In-place algorithm: normalize out-of-range values, then use index-sign
        marking to record presence. Time O(n), extra space O(1).
        """
        n = len(nums)

        # Phase 1a: Check for 1. This is crucial because we use 1 as a
        # sentinel value. If 1 is missing, it's the answer.
        if 1 not in nums:
            return 1

        # Phase 1b: Normalize. Replace negatives, zeros, and values > n
        # with our safe sentinel value, 1.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Phase 2: Mark. Use index as a hash key and sign to mark presence.
        for i in range(n):
            # Get the value, make sure it's positive
            val = abs(nums[i])
            idx = val - 1

            # Mark the index by making it negative.
            # Only do it if it's not already negative.
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Phase 3: Find. The first index with a positive value
        # indicates the missing integer (i + 1).
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # Phase 4: Edge Case. If all 1..n are present (all are negative),
        # then the answer is n+1.
        return n + 1


if __name__ == "__main__":
    tests = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([2], 1),
        ([1], 2),
        ([], 1),
    ]
    for arr, expected in tests:
        res = Solution().firstMissingPositive(arr.copy())
        print(f"{arr} -> {res} (expected {expected})")
