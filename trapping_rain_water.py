from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1

            max_left[i] = l_wall
            max_right[j] = r_wall

            l_wall = max(max_left[i], height[i])
            r_wall = max(max_right[j], height[j])

        total_sum = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            total_sum += max(0, pot - height[i])
        return total_sum


height_array = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
print(Solution().trap(height_array))
