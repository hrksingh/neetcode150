from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # Ensure A is the smaller array
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2  # Number of elements from A
            j = half - i  # Number of elements from B

            # Boundary conditions: use -inf and +inf for out of bounds
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            # Check if partition is correct
            if A_left <= B_right and B_left <= A_right:
                # Odd total elements
                if total % 2:
                    return min(A_right, B_right)
                # Even total elements
                return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
        return -1.0


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(Solution().findMedianSortedArrays(nums1, nums2))
