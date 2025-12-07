from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Find k closest elements to x in sorted array arr.
        Binary-search over the window start index. Time O(log(n-k) + k), space O(k).
        Tie-breaking: smaller elements preferred (leftmost window).
        """
        n = len(arr)
        if k >= n:
            return arr

        # search range for leftmost start index of a window of size k
        left, right = 0, n - k
        while left < right:
            mid = left + (right - left) // 2
            # if left edge is farther than right edge, move window right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, 10, [2, 3, 4, 5]),
        ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4]),
    ]
    for arr, k, x, expected in tests:
        out = sol.findClosestElements(arr, k, x)
        print(f"arr={arr} k={k} x={x} -> {out} expected={expected}")
        assert out == expected
