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
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if heap:
                proc_time, curr_idx = heapq.heappop(heap)
                time += proc_time
                res.append(curr_idx)
            else:
                time = tasks[i][0]
        return res


if __name__ == "__main__":
    # tasks = [[1, 4], [3, 3], [2, 1]]
    tasks2 = [[1, 2], [2, 4], [3, 2], [4, 1]]
    print(Solution().getOrder(tasks2))  # output = [0,2,3,1]
