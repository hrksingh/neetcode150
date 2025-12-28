from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subArr = 1
            curSum = 0

            for num in nums:
                curSum += num
                if curSum > largest:
                    subArr += 1
                    if subArr > k:
                        return False
                    curSum = num
            return True

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if canSplit(mid):
                r = mid
            else:
                l = mid + 1
        return l


nums = [1, 2, 3, 4, 5]
k = 2
Output = 9
print(Solution().splitArray(nums, k) == Output)
