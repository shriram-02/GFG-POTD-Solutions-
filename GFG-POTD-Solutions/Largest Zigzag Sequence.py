class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)
        dp = mat[0][:]

        for i in range(1, n):
            best1 = max(dp)
            idx1 = dp.index(best1)
            best2 = max(dp[j] for j in range(n) if j != idx1)

            new_dp = [0] * n
            for j in range(n):
                new_dp[j] = mat[i][j] + (best2 if j == idx1 else best1)

            dp = new_dp

        return max(dp)