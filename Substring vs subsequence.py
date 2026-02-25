"""
Demonstrates the difference between substrings and subsequences.

Definitions:
- Substring: contiguous characters from the original string.
- Subsequence: characters from the original string in order, not necessarily contiguous.

Complexity:
- Generating all substrings: O(n^2) time, O(n^2) space (number of substrings ~ n*(n+1)/2).
- Generating all subsequences: O(2^n) time, O(2^n) space (each character can be present/absent).

Example:
Input: x = "abcd"
Substrings: ['a','ab','abc','abcd','b','bc','bcd','c','cd','d']
Subsequences: ['', 'a','b','ab','c','ac','bc','abc','d','ad','bd','abd','cd','acd','bcd','abcd']
"""

x = "abcd"  # example input
n = len(x)

substring = []
subsequence = [""]  # start with empty subsequence to build upon

# Generate all substrings (contiguous slices)
for i in range(n):
    # j goes from i+1 to n (slice end is exclusive), so x[i:j] is every substring starting at i
    for j in range(i + 1, n + 1):
        substring.append(x[i:j])


# Generate all subsequences using the doubling technique:
# for each character, append it to all existing subsequences to create new ones
for char in x:
    current_count = len(subsequence)
    for i in range(current_count):
        # take existing subsequence and extend it by the current char
        new_sub = subsequence[i] + char
        subsequence.append(new_sub)

# Print results for the example
print(f"substring: {substring}")
print(f"subsequence: {subsequence}")
