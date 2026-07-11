class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        n, m = len(mat), len(mat[0])

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        ans = -1
        vis = [[False] * m for _ in range(n)]

        def dfs(x, y, dist):
            nonlocal ans

            if x == xd and y == yd:
                ans = max(ans, dist)
                return

            vis[x][y] = True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1 and not vis[nx][ny]:
                    dfs(nx, ny, dist + 1)

            vis[x][y] = False

        dfs(xs, ys, 0)
        return ans