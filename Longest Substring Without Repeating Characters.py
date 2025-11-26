class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores {character: index}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # If duplicate is found AND it's inside the current window
            if char in char_map and char_map[char] >= left:
                # Jump left pointer directly past the previous occurrence
                left = char_map[char] + 1

            # Update the last seen index of the character
            char_map[char] = right

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
