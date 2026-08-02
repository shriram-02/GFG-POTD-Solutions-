class Solution:
    def count(self, n: int, m: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for x in range(1, m + 1):
            dp[1][x] = 1
        
        adj = [[] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if i % j == 0 or j % i == 0:
                    adj[i].append(j)
        
        for length in range(2, n + 1):
            for last in range(1, m + 1):
                for prev in adj[last]:
                    dp[length][last] += dp[length - 1][prev]
        
        return sum(dp[n][1:])