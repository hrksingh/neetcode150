import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]


# Test code
if __name__ == "__main__":
    commands = ["KthLargest", "add", "add", "add", "add", "add"]
    params = [[3, [1, 2, 3, 3]], [3], [5], [6], [7], [8]]

    results = []
    kth_largest: KthLargest = None  # type: ignore

    for i, cmd in enumerate(commands):
        if cmd == "KthLargest":
            kth_largest = KthLargest(params[i][0], params[i][1])
            results.append(None)
        else:  # "add"
            if kth_largest is not None:
                result = kth_largest.add(params[i][0])
            results.append(result)

    print(results)
