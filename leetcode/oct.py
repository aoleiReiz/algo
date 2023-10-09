from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_min = prices[0]
        for price in prices[1:]:
            if price < cur_min:
                cur_min = price
            else:
                max_profit = max(max_profit, price - cur_min)
        return max_profit