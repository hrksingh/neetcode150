from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Return the minimum integer eating speed k such that Koko can eat
        all `piles` within `h` hours.

        Uses binary search over possible speeds. Time O(n log m) where m = max(piles).
        """
        if not piles:
            return 0

        left = 1
        right = max(piles)  # upper bound for eating speed

        def can_finish(speed: int) -> bool:
            # compute total hours needed at given speed (use integer math)
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
                if hours > h:  # early exit if already too slow
                    return False
            return hours <= h

        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left


piles = [1, 4, 3, 2]
h = 9

print(Solution().minEatingSpeed(piles, h) == 2)
