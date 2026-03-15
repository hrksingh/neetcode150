from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def dfs(i, curr, total):
            if target == total:
                res.append(curr.copy())
                return

            if total > target or i == n:
                return

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    candidates = [9, 2, 2, 4, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
