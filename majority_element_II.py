from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Return all elements that appear more than n/3 times.

        Algorithm:
        - Phase 1 (candidate selection): use the Boyer–Moore majority vote extension
          to find up to two potential candidates. If an element appears > n/3 times,
          it must be one of these candidates.
        - Phase 2 (validation): count occurrences of the candidates and return those
          that exceed the n/3 threshold.

        Complexity: O(n) time, O(1) extra space.
        """
        if not nums:
            return []

        # Two candidates and their counters (initially unset / zero).
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0

        # Phase 1: pick up to two potential candidates.
        for num in nums:
            if num == candidate1:
                # increment counter if current number matches candidate1
                count1 += 1
            elif num == candidate2:
                # increment counter if current number matches candidate2
                count2 += 1
            elif count1 == 0:
                # no current candidate1 — assign num to candidate1
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                # no current candidate2 — assign num to candidate2
                candidate2 = num
                count2 = 1
            else:
                # num matches neither candidate and both counters > 0:
                # decrease both counters (this cancels out a potential majority vote)
                count1 -= 1
                count2 -= 1

        # Phase 2: verify actual counts of the chosen candidates.
        res = []
        count1, count2 = 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1

        # An element must appear strictly more than floor(n/3) times to qualify.
        threshold = len(nums) // 3
        if count1 > threshold:
            res.append(candidate1)
        # ensure we don't append the same candidate twice (can happen if one candidate is None)
        if candidate2 is not None and candidate2 != candidate1 and count2 > threshold:
            res.append(candidate2)

        return res


nums = [5, 2, 3, 2, 2, 2, 2, 5, 5, 5]
print(Solution().majorityElement(nums))
