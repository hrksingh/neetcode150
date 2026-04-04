from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len(nums) == len(sol):
                res.append(sol.copy())
                return

            for num in count:
                if count[num] > 0:
                    sol.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    sol.pop()

        dfs()
        return res


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
