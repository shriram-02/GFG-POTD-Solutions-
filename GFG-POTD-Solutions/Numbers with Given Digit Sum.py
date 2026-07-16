class Solution:
    def countWays(self, n, sum):
        if sum > 9 * n or sum < 1:
            return -1

        dp = [[0] * (sum + 1) for _ in range(n + 1)]

        for d in range(1, 10):
            if d <= sum:
                dp[1][d] = 1

        for i in range(2, n + 1):
            for s in range(sum + 1):
                for d in range(10):
                    if s >= d:
                        dp[i][s] += dp[i - 1][s - d]

        return dp[n][sum] if dp[n][sum] else -1