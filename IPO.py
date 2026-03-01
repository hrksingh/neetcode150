import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        max_profit = []
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)
        for _ in range(k):
            while min_capital and min_capital[0][0] <= w:
                _, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -p)
            if not max_profit:
                break

            w += -heapq.heappop(max_profit)

        return w


if __name__ == "__main__":
    k = 4
    w = 2
    profit = [2, 3, 1, 5, 3]
    capital = [4, 4, 2, 3, 3]
    print(Solution().findMaximizedCapital(k, w, profit, capital))  # Output = 14
