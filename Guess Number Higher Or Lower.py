# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        """Find the picked number in range [1, n] using the `guess` API.

        Uses binary search. Returns the picked number or -1 if not found.
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == -1:
                # mid is higher than the picked number
                right = mid - 1
            elif res == 1:
                # mid is lower than the picked number
                left = mid + 1
            else:
                return mid
        return -1


# --- Testing helper (mock of the guess API) ---
PICKED: int | None = None


def guess(num: int) -> int:
    """Mock guess API for local testing. Compares `num` to global PICKED.

    Returns:
    -1 if num is higher than the picked number
     1 if num is lower than the picked number
     0 if num == picked
    """
    if PICKED is None:
        raise RuntimeError("PICKED not set for guess() mock")
    if num > PICKED:
        return -1
    if num < PICKED:
        return 1
    return 0


if __name__ == "__main__":
    # small tests
    for n, picked in [(10, 6), (1, 1), (2, 2), (100, 73)]:
        PICKED = picked
        ans = Solution().guessNumber(n)
        print(f"n={n} picked={picked} -> guessNumber -> {ans}")
