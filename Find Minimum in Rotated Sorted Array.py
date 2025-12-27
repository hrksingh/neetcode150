from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # Binary search for the inflection point
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                # Mid is in the left sorted portion, min is to the right
                l = mid + 1
            else:
                # Mid could be the min, or min is to the left
                r = mid

        # l == r at this point, both point to minimum
        return nums[l]


nums = [3, 4, 5, 6, 1, 2]
Output = 1
print(Solution().findMin(nums) == Output)
