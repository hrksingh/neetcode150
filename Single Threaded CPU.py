from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            tasks[i].append(i)
        tasks.sort(key=lambda t: t[0])
        print(tasks)
        res = []
        return res


if __name__ == "__main__":
    tasks = [[1, 4], [3, 3], [2, 1]]
    print(Solution().getOrder(tasks))
