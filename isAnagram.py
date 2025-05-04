class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for letter in s:
            sMap[letter] = sMap.get(letter, 0) + 1

        for letter in t:
            tMap[letter] = tMap.get(letter, 0) + 1
 
        return sMap == tMap
    
    
Solution().isAnagram("racecar", "carrace")