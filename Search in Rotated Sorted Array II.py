from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            # Found target
            if target == nums[mid]:
                return True

            # Left half is definitely sorted
            elif nums[l] < nums[mid]:
                # Check if target is in sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Right half is definitely sorted
            elif nums[l] > nums[mid]:
                # Check if target is in sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            # Ambiguous case: nums[l] == nums[mid]
            # Cannot determine which half is sorted
            else:
                l += 1  # Skip one duplicate

        return False


nums = [4, 5, 5, 6, 1, 1, 2, 3, 3]
target = 5
print(Solution().search(nums, target))

nums1 = [1, 1, 1, 1, 1, 1, 1]
target1 = 1
print(Solution().search(nums1, target1))

nums2 = [1, 1, 1, 1, 1, 1, 1]
target2 = 2
print(Solution().search(nums2, target2))
