from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 'l' is the buy day, 'r' is the sell day
        l, r = 0, 1
        maxP = 0  # Use a more standard variable name like maxP or max_profit

        while r < len(prices):
            # Check if we have a profitable situation
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # If prices[r] is lower, it's a better day to buy.
                # So, we move our buy pointer 'l' up to 'r'.
                l = r

            # Move the sell pointer 'r' forward to check the next day
            r += 1

        return maxP
