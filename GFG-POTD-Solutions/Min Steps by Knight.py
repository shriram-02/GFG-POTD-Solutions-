class Solution:
    def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
        # Code here
        from collections import deque

        if knightPos == targetPos:
            return 0

        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        sx, sy = knightPos[0] - 1, knightPos[1] - 1
        tx, ty = targetPos[0] - 1, targetPos[1] - 1

        q = deque([(sx, sy, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[sx][sy] = True

        while q:
            x, y, steps = q.popleft()

            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if nx == tx and ny == ty:
                        return steps + 1

                    visited[nx][ny] = True
                    q.append((nx, ny, steps + 1))

        return -1