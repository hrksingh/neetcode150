from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, n - 1

            while lo < hi:
                tSum = nums[i] + nums[lo] + nums[hi]
                if tSum > 0:
                    lo += 1
                elif tSum < 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1

        return res


if __name__ == "__main__":
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ]

    sol = Solution()

    def _normalize(triples):
        # sort elements inside each triplet and return a set of tuples for order-independent comparison
        return {tuple(sorted(t)) for t in triples}

    for inp, expected in tests:
        out = sol.threeSum(inp.copy())
        ok = _normalize(out) == _normalize(expected)
        print(f"{inp} -> {out} (expected {expected}) {'OK' if ok else 'FAIL'}")
        assert ok, f"Test failed for input: {inp}"
