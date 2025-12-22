from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Compute largest rectangle area in a histogram.
        Uses a monotonic increasing stack of (start_index, height). Time O(n), space O(n).
        """
        max_area = 0
        stack: List[tuple[int, int]] = []
        length = len(heights)

        for current_index, current_height in enumerate(heights):
            start = current_index
            while stack and current_height < stack[-1][1]:
                index, height = stack.pop()
                width = current_index - index
                max_area = max(max_area, height * width)
                start = index
            stack.append((start, current_height))

        # These survived till end of array
        while stack:
            start_index, height = stack.pop()
            width = length - start_index
            max_area = max(max_area, height * width)

        return max_area


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
