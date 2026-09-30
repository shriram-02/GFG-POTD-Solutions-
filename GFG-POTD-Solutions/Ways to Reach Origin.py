class Solution:
    def ways(self, x: int, y: int) -> int:
        # code here
        MOD = 10**9 +7
        dp = [1] * (y + 1)
        for i in range(1, x + 1):
            for j in range(1,y + 1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD
        return dp[y]