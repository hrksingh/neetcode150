class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        # Use arrays of size 26 for constant time O(1) character mapping
        s1_count = [0] * 26
        s2_count = [0] * 26

        def char_to_idx(char):
            """Helper function to map a character to its 0-25 index."""
            return ord(char) - ord("a")

        # 1. Initialize the maps with the first window (size n1)
        for i in range(n1):
            s1_count[char_to_idx(s1[i])] += 1
            s2_count[char_to_idx(s2[i])] += 1

        # 2. Check the initial window
        if s1_count == s2_count:
            return True

        # 3. Slide the window one step at a time
        # i acts as the right pointer (R) index for the character being added
        for i in range(n1, n2):
            # Add the new character (R)
            s2_count[char_to_idx(s2[i])] += 1

            # Remove the old character (L), which is at index i - n1
            s2_count[char_to_idx(s2[i - n1])] -= 1

            # Check for a match (O(26) comparison, still O(1) time)
            if s2_count == s1_count:
                return True

        return False
