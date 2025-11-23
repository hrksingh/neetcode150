from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            hl, hr = heights[l], heights[r]

            if hl < hr:
                max_area = max(max_area, (r - l) * hl)
                l += 1
            else:
                max_area = max(max_area, (r - l) * hr)
                r -= 1

        return max_area


if __name__ == "__main__":
    height = [1, 7, 2, 5, 4, 7, 3, 6]
    print(Solution().maxArea(height))
