class Solution:
    def shortestDist(self, mat):
        n = len(mat)
        ans = [[0] * n for _ in range(n)]
        vis = [[False] * n for _ in range(n)]

        def dfs(i, j):
            if i == n - 1 and j == n - 1:
                ans[i][j] = 1
                return True

            if vis[i][j] or mat[i][j] == 0:
                return False

            vis[i][j] = True
            ans[i][j] = 1

            jump = mat[i][j]

            for k in range(1, jump + 1):
                if j + k < n and dfs(i, j + k):
                    return True

                if i + k < n and dfs(i + k, j):
                    return True

            ans[i][j] = 0
            return False

        if mat[0][0] == 0 or not dfs(0, 0):
            return [[-1]]

        return ans