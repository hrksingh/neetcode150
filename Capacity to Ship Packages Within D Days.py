from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """Find minimum ship capacity to ship `weights` within `days` days.

        Binary-search the minimal capacity between max(weights) and sum(weights).
        """

        def can_ship(capacity: int) -> bool:
            days_needed = 1
            cur_load = 0
            for w in weights:
                cur_load += w
                if cur_load > capacity:
                    cur_load = w
                    days_needed += 1
                    if days_needed > days:  # early exit
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left


weights = [1, 5, 4, 4, 2, 3]
days = 3
print(Solution().shipWithinDays(weights, days))
