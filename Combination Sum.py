from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, sol, total):
            if total == target:
                res.append(sol[:])
                return

            if total > target or i == n:
                return

            sol.append(nums[i])
            dfs(i, sol, total + nums[i])
            sol.pop()

            dfs(i + 1, sol, total)

        dfs(0, [], 0)
        return res

    def combinationSumOptimized(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. Sort the input to allow for pruning
        nums.sort()
        n = len(nums)

        def dfs(i, sol, total):
            if total == target:
                res.append(list(sol))
                return

            for j in range(i, n):
                # 2. Pruning: If adding this number exceeds target,
                # all subsequent numbers will also exceed it.
                if total + nums[j] > target:
                    break

                sol.append(nums[j])
                # We pass 'j' instead of 'j + 1' to allow reusing the same element
                dfs(j, sol, total + nums[j])
                sol.pop()

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    nums = [2, 5, 6, 9]
    target = 9
    print(Solution().combinationSum(nums, target))
