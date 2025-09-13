from typing import List, Optional
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

# Boyer-Moore Voting Algorithm
class OptimalSolution:
    def majorityElement(self, nums: List[int]) -> Optional[int]:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        # (Optional: verify candidate actually appears > n/2)
        return candidate
                
print(OptimalSolution().majorityElement([5,5,1,1,1,5,5]))
print(OptimalSolution().majorityElement([2,2,2]))      