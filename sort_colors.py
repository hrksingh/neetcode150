from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # If it's a 0, swap with the low pointer
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1  # Increment mid because we know nums[low] was not a 2
            elif nums[mid] == 1:
                # If it's a 1, it's in the right place, just move on
                mid += 1
            else:
                # If it's a 2, swap with the high pointer
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                # DO NOT increment mid, as the new nums[mid] needs to be checked


arr = [2, 0, 2, 1, 1, 0]
Solution().sortColors(arr)
print(arr)
