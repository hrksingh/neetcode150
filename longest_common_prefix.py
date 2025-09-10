from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs:
                if i == len(word) or prefix[i] != word[i]:
                    return prefix[:i]
        return prefix
    
print(Solution().longestCommonPrefix(["flow", "flower", "flog", "flight"])) # this example for prefix[i] != word[i]
print(Solution().longestCommonPrefix(["flow", "flower", "flog", "fl"])) # this example for i == len(word)

class OptimalSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # in-place sort (use .sort(key=str.lower) for case-insensitive)
        strs.sort()
        first, last = strs[0], strs[-1]
        min_len = min(len(first), len(last))
           
        for i in range(min_len):
            if first[i] != last[i]:
                return first[:i]
        return first[:min_len]
    
print(OptimalSolution().longestCommonPrefix(["flow", "flower", "flog", "flight"]))
print(OptimalSolution().longestCommonPrefix(["flow", "flower", "flog", "fli"]))