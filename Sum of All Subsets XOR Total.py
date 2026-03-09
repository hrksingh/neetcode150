from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, xor):
            if i == n:
                return xor

            exclude = dfs(i + 1, xor)
            include = dfs(i + 1, nums[i] ^ xor)
            return include + exclude

        return dfs(0, 0)

    def subsetXORSumUsingORandBitShift(self, nums: List[int]) -> int:
        bor = 0
        for num in nums:
            bor |= num
        return bor << len(nums) - 1


if __name__ == "__main__":
    nums = [3, 1, 1]
    print(Solution().subsetXORSum(nums))  # Output: 12
    print(Solution().subsetXORSumUsingORandBitShift(nums))  # Output: 12
