from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        frequencyBucket = [ [] for i in range(len(nums)+1)]
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        for key, value in counter.items():
            frequencyBucket[value].append(key)

        res = []

        for i in range(len(frequencyBucket) - 1, 0, -1):
            for num in frequencyBucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

print(Solution().topKFrequent([1,1,1,2,2,3], 2))
