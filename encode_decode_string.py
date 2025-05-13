from typing import List


class Solution:
    dem = '#'
    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for s in strs:
            length = str(len(s))
            res_str += length + self.dem + s
        return res_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.dem:
                j += 1
            fetchLen = int(s[i:j])
            demPos = j
            nextPoint = demPos + fetchLen + 1
            res.append(s[demPos+1 : nextPoint])
            i = nextPoint
        return res

e = Solution().encode(["hello","world#again", "notdem#again"])
print(e)
d = Solution().decode(e)
print(d)