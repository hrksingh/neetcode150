from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, v in enumerate(nums):
            # check against the previous at-most-k elements
            if v in seen:
                return True
            seen.add(v)
            # maintain window of size <= k (previous k items)
            if i >= k:
                seen.remove(nums[i - k])
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3
    print(Solution().containsNearbyDuplicate(nums, k))
