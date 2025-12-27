from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            # Handle the ambiguous case first
            if nums[l] == nums[mid] == nums[r]:
                # Can't determine which side is sorted
                # Skip the duplicate and continue
                l += 1
                r -= 1
                continue

            # Now we can safely determine which half is sorted
            if nums[l] < nums[mid]:
                # Left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Target in left sorted half
                else:
                    l = mid + 1  # Target in right half
            else:
                # Right half is sorted (nums[l] > nums[mid])
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Target in right sorted half
                else:
                    r = mid - 1  # Target in left half

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
