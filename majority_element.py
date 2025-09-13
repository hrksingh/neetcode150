from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        threshold = len(nums) // 2
        num = nums[0]
        for num in nums:
            counter[num] += 1
            if counter[num] > threshold:
                return num
        return num

print(Solution().majorityElement([5,5,1,1,1,5,5]))
print(Solution().majorityElement([2,2,2]))