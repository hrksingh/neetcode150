from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res, sol = [], []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i == len(digits):
                res.append("".join(sol))
                return

            for char in digitToChar[digits[i]]:
                sol.append(char)
                dfs(i + 1)
                sol.pop()

        dfs(0)
        return res
