from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l


Input1 = [1, 3, 5, 6]
target1 = 5
Output1 = 2
print(Solution().searchInsert(Input1, target1) == Output1)

Input2 = [1, 3, 5, 6]
target2 = 2
Output2 = 1
print(Solution().searchInsert(Input2, target2) == Output2)

Input3 = [1, 3, 5, 6]
target3 = 7
Output3 = 4
print(Solution().searchInsert(Input3, target3) == Output3)
