class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        n, m = len(mat), len(mat[0])

        # Prefix sum
        ps = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                ps[i + 1][j + 1] = (
                    mat[i][j]
                    + ps[i][j + 1]
                    + ps[i + 1][j]
                    - ps[i][j]
                )

        def get_sum(r1, c1, r2, c2):
            return (
                ps[r2 + 1][c2 + 1]
                - ps[r1][c2 + 1]
                - ps[r2 + 1][c1]
                + ps[r1][c1]
            )

        ans = []

        for i, j in queries:
            # If even the 1x1 square is invalid
            if mat[i][j] > k:
                ans.append(-1)
                continue

            max_r = min(i, n - 1 - i, j, m - 1 - j)

            lo, hi = 0, max_r
            best = 0

            while lo <= hi:
                r = (lo + hi) // 2

                r1 = i - r
                c1 = j - r
                r2 = i + r
                c2 = j + r

                if get_sum(r1, c1, r2, c2) <= k:
                    best = r
                    lo = r + 1
                else:
                    hi = r - 1

            ans.append(2 * best + 1)

        return ans