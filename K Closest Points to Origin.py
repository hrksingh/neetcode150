import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def dist_and_point(x, y):
            return (-(x**2 + y**2), [x, y])

        for x, y in points:
            if len(heap) < k:
                heapq.heappush(heap, dist_and_point(x, y))
            else:
                heapq.heappushpop(heap, dist_and_point(x, y))
        return [point for _, point in heap]


if __name__ == "__main__":
    points = [[0, 2], [2, 2]]
    k = 1
    print(Solution().kClosest(points, k))
