import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, _ in enumerate(tasks):
            tasks[i].append(i)
        tasks.sort(key=lambda t: t[0])

        heap, res = [], []
        time, i = 0, 0
        while heap or i < len(tasks):
            if not heap:
                time = tasks[i][0]

            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if heap:
                proc_time, curr_idx = heapq.heappop(heap)
                time += proc_time
                res.append(curr_idx)
        return res


if __name__ == "__main__":
    tasks = [[1, 4], [3, 3], [2, 1]]
    print(Solution().getOrder(tasks))
