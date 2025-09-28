from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products and multiply with prefix in result
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix  # here res[i] will act as prefix so prefix * suffix
            suffix *= nums[i]  # calculating suffix for next number

        return res


print(Solution().productExceptSelf([1, 2, 4, 6]))
