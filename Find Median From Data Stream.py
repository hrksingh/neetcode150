import heapq


class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half (as negative values)
        # min_heap stores the larger half
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 1. Add to max_heap
        heapq.heappush(self.max_heap, -num)

        # 2. Ensure max_heap elements are <= min_heap elements
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # 3. Balance sizes: max_heap can have at most one more element than min_heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
