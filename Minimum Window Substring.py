from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case handling
        if not t or not s or len(s) < len(t):
            return ""

        countT = Counter(t)  # Frequency map for the target string
        window = defaultdict(int)  # Current window frequency map

        have, need = 0, len(countT)
        l = 0
        best_len, best_start = float("inf"), 0  # (length, start_index)

        for r, ch in enumerate(s):
            if ch in countT:  # only track characters that actually exist in t
                window[ch] += 1
                if window[ch] == countT[ch]:
                    have += 1

            # While the window is valid, try to minimize it
            while have == need:
                curr_len = r - l + 1
                if ( curr_len < best_len ):  # Update our result if the current window is smaller
                    best_len = curr_len
                    best_start = l

                # Shrink the window from the left
                left_char = s[l]
                if left_char in countT:
                    window[left_char] -= 1
                    if (window[left_char] < countT[left_char]):  # If count drops below required, the window is no longer valid
                        have -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_start : best_start + best_len]


if __name__ == "__main__":
    tests = [
        ("OUZODYXAZV", "XYZ", "YXAZ"),
        ("ADOBECODEBANC", "ABC", "BANC"),  # standard reference case [web:64]
        # . Exact match, whole string
        ("ABC", "ABC", "ABC"),
        # t longer than s → no window
        ("AB", "ABC", ""),
        # No possible window (character missing)
        ("ABCDEF", "XZ", ""),
        # Repeated characters required
        ("AAABBC", "AABC", "AABBC"),  # need 2 A's, 1 B, 1 C
        # Case sensitivity check
        ("aAaAaA", "Aa", "aA"),
        # Single-character t
        ("BBBBBACCC", "A", "A"),
    ]

    sol = Solution()
    for i, (s, t, expected) in enumerate(tests, 1):
        out = sol.minWindow(s, t)
        status = "OK" if out == expected else "FAIL"
        print(f"Test {i}: s={s!r}, t={t!r}")
        print(f"  Output:   {out!r}")
        print(f"  Expected: {expected!r}")
        print(f"  Status:   {status}")
        print("-" * 40)
