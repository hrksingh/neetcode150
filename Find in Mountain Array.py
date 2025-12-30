# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


from functools import lru_cache


class MountainArray:
    """Simple in-memory implementation of the MountainArray API for testing.

    Provides `get(index)` and `length()` methods expected by the problem.
    """

    def __init__(self, arr):
        self._arr = list(arr)

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self._arr):
            raise IndexError("index out of bounds")
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)


class Solution:
    def findInMountainArray(self, target: int, mountainArr: "MountainArray") -> int:
        n = mountainArr.length()

        @lru_cache(maxsize=None)
        def get(idx: int) -> int:
            return mountainArr.get(idx)

        # Find peak index using standard while left < right pattern.
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        # Binary search on ascending part [0..peak]
        def bin_search_asc(lo: int, hi: int) -> int:
            while lo <= hi:
                mid = (lo + hi) // 2
                val = get(mid)
                if val == target:
                    return mid
                if val < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        # Binary search on descending part [peak+1..n-1]
        def bin_search_desc(lo: int, hi: int) -> int:
            while lo <= hi:
                mid = (lo + hi) // 2
                val = get(mid)
                if val == target:
                    return mid
                if val > target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        # Try ascending side (includes peak)
        idx = bin_search_asc(0, peak)
        if idx != -1:
            return idx

        # Try descending side
        return bin_search_desc(peak + 1, n - 1)
