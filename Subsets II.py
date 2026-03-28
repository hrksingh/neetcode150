from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Essential for skipping duplicates

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            # 1. Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # 2. Decision NOT to include nums[i]
            # Skip all duplicates of the current element
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return res


if __name__ == "__main__":
    nums = [1, 2, 1]
    print(Solution().subsetsWithDup(nums))
