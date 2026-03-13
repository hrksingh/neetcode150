from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []

        def backtrack(i):
            if i == n:
                res.append(subset[:])
                return

            # don't make a choice to include a value
            backtrack(i + 1)

            # make a choice to include a value
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

        backtrack(0)
        return res

    def subsetsIterative(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            current = res[:]
            for subset in current:
                res.append(subset + [num])
        return res


if __name__ == "__main__":
    nums = [1, 3, 5]
    # print(Solution().subsets(nums))
    print(Solution().subsetsIterative(nums))
