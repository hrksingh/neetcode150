from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums[:] = nums[n - k :] + nums[: n - k]


nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, 3)
print(nums)
