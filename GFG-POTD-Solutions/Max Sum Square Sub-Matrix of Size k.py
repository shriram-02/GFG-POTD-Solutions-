class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)

        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        ans = float("-inf")

        for i in range(n - k + 1):
            for j in range(n - k + 1):
                s = (
                    prefix[i + k][j + k]
                    - prefix[i][j + k]
                    - prefix[i + k][j]
                    + prefix[i][j]
                )
                ans = max(ans, s)

        return ans