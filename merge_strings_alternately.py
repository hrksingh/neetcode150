class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []

        # Merge until one word is exhausted
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # Append the remainder of both words (one will be empty)
        # Slicing from the current index captures the tail.
        res.append(word1[i:])
        res.append(word2[j:])

        # Fast string construction
        return "".join(res)
