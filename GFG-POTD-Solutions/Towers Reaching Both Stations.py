from collections import deque

class Solution:
    def countCoordinates(self, mat):
        n, m = len(mat), len(mat[0])

        def bfs(starts):
            vis = [[False] * m for _ in range(n)]
            q = deque()

            for x, y in starts:
                if not vis[x][y]:
                    vis[x][y] = True
                    q.append((x, y))

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n and
                        0 <= ny < m and
                        not vis[nx][ny] and
                        mat[nx][ny] >= mat[x][y]
                    ):
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return vis

        p = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]
        q = [(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)]

        visP = bfs(p)
        visQ = bfs(q)

        ans = 0
        for i in range(n):
            for j in range(m):
                if visP[i][j] and visQ[i][j]:
                    ans += 1
        return ans