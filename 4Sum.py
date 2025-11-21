from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        if n < 4:
            return res

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # prune: smallest possible sum too large
            # If this sum is already larger than target, there’s no point in continuing:
            # any sum you can make with a higher i will be even larger (since numbers are sorted),
            # so you break the outer loop.
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # prune: largest possible sum too small
            # if you fix nums[i], the largest possible sum you can get is nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] (the biggest values left).
            # If this is still smaller than target, no possible combination with the current i will work, so skip (continue to next larger i).
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # prune inner loop
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                lo, hi = j + 1, n - 1
                while lo < hi:
                    four_sum = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    elif four_sum < target:
                        lo += 1
                    else:
                        hi -= 1

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    for target in (0, 3):
        res = sol.fourSum(nums.copy(), target)
        print(f"nums={nums} target={target} -> {res}")
