class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9 + 7
        n, m = len(matrix), len(matrix[0])

        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                pre[i][j] = (
                    matrix[i][j]
                    + pre[i + 1][j]
                    + pre[i][j + 1]
                    - pre[i + 1][j + 1]
                )

        dp = [[[0] * m for _ in range(n)] for _ in range(k)]

        for i in range(n):
            for j in range(m):
                dp[0][i][j] = 1 if pre[i][j] > 0 else 0

        for cuts in range(1, k):
            for i in range(n):
                for j in range(m):
                    if pre[i][j] == 0:
                        continue
                    ways = 0

                    for r in range(i + 1, n):
                        if pre[i][j] - pre[r][j] > 0:
                            ways = (ways + dp[cuts - 1][r][j]) % MOD

                    for c in range(j + 1, m):
                        if pre[i][j] - pre[i][c] > 0:
                            ways = (ways + dp[cuts - 1][i][c]) % MOD

                    dp[cuts][i][j] = ways

        return dp[k - 1][0][0]