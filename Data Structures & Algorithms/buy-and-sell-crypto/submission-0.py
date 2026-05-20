class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []; profit = 0
        for price in prices:
            if not stack:
                stack.append(price)
            else:
                top = stack[-1]
                if price < top:
                    stack.append(price)
                else:
                    p = price - top; profit = max(profit, p)
        return profit

        