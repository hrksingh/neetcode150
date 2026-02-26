import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(max_heap)

        res = []
        prev = None  # holds a (cnt, ch) tuple to re‑insert

        while max_heap:
            cnt, ch = heapq.heappop(max_heap)
            res.append(ch)

            # push the previous leftover back before we change current
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            cnt += 1  # increment toward zero
            if cnt != 0:  # still have more of this char
                prev = (cnt, ch)

        # if we’re holding a leftover and nothing else to place, impossible
        if prev:
            return ""
        return "".join(res)


if __name__ == "__main__":
    print(Solution().reorganizeString("abbccdd"))
    print(Solution().reorganizeString("aaab"))  # -> ""
