import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Line sweep Algorithm
        pass_change = [0] * 1001
        for num_pass, start, end in trips:
            pass_change[start] += num_pass
            pass_change[end] -= num_pass

        cur_pass = 0
        for i in range(1001):
            cur_pass += pass_change[i]
            if cur_pass > capacity:
                return False
        return True

    def carPoolingHeap(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        curr = 0
        min_heap = []
        for num_pass, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                curr -= min_heap[0][1]
                heapq.heappop(min_heap)

            curr += num_pass
            if curr > capacity:
                return False
            heapq.heappush(min_heap, (end, num_pass))
        return True


if __name__ == "__main__":
    print(Solution().carPooling([[4, 1, 2], [3, 2, 4]], 4))
    print(Solution().carPooling([[2, 1, 3], [3, 2, 4]], 4))
    print(Solution().carPoolingHeap([[4, 1, 2], [3, 2, 4]], 4))
    print(Solution().carPoolingHeap([[2, 1, 3], [3, 2, 4]], 4))
