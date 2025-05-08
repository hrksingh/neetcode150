from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        res = defaultdict(list)
        
        for str in strs:
            count = [0]*26
            for char in str:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(str)
        return list(res.values())
    
# Test the function
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))