from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseString_slice(self, s: List[str]) -> None:
        """Readable one-liner that mutates the list via slice assignment."""
        s[:] = s[::-1]


if __name__ == "__main__":
    tests = [
        (list("hello"), list("olleh")),
        ([], []),
        (list("a"), list("a")),
    ]
    sol = Solution()
    for inp, expected in tests:
        arr = inp.copy()
        sol.reverseString(arr)
        print("ok" if arr == expected else f"fail: {arr} != {expected}")
