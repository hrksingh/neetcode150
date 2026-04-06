from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        def dfs(open, close):
            if close == open == n:
                res.append("".join(sol))
                return

            if open < n:
                sol.append("(")
                dfs(open + 1, close)
                sol.pop()

            if close < open:
                sol.append(")")
                dfs(open, close + 1)
                sol.pop()

        dfs(0, 0)
        return res


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
