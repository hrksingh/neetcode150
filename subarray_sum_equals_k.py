from typing import List


class Solution:
    def subArraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = {0: 1}

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res


print(Solution().subArraySum([1, -1, 1, 1, 1, 1], 3))
