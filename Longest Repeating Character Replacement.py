from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        # Stores frequency of characters in the current window
        char_map = defaultdict(int)
        l = 0  # Left pointer
        max_f = 0  # Maximum frequency of any character in the current window

        for r in range(len(s)):
            char_map[s[r]] += 1

            # max_f is updated only when expanding (optimisation)
            max_f = max(max_f, char_map[s[r]])

            window_len = (r - l) + 1
            # Non-majority count = number of chars we must replace
            replacements_needed = window_len - max_f

            # If replacements needed > k, the window is invalid. Shrink from the left.
            if replacements_needed > k:
                # Remove character at left pointer
                char_map[s[l]] -= 1
                # Slide the left pointer
                l += 1

            # The maximum length is only updated when the window is valid.
            # If the window shrinks, 'longest' won't increase, which is fine.
            # If it's valid, the current window length is a candidate for the longest.
            longest = max(longest, r - l + 1)

        return longest
