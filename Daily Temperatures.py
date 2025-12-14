from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores indices

        for i, t in enumerate(temperatures):
            # While stack is not empty AND current temp > temp at stack top
            while stack and temperatures[stack[-1]] < t:
                sIndex = stack.pop()
                res[sIndex] = i - sIndex
            stack.append(i)
        return res


temperatures = [30, 38, 30, 36, 35, 40, 28]
print(Solution().dailyTemperatures(temperatures))
