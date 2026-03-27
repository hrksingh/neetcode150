from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack():
            if n == len(sol):
                res.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
