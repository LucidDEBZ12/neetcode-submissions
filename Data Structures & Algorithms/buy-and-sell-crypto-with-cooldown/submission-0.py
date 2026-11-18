
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):

            # Can BUY
            buy = -prices[i] + dp[i + 1][0]
            skip = dp[i + 1][1]

            dp[i][1] = max(buy, skip)

            # HOLDING (can SELL)
            sell = prices[i] + dp[i + 2][1]
            skip = dp[i + 1][0]

            dp[i][0] = max(sell, skip)

        return dp[0][1]
