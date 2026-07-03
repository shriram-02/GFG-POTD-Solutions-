class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        f = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])

        b = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    b[i][j] = b[i + 1][j + 1] + 1
                else:
                    b[i][j] = max(b[i + 1][j], b[i][j + 1])

        lcs = f[n1][n2]
        ans = 0

        for i in range(n1 + 1):
            seen = set()
            for j in range(n2):
                if s2[j] not in seen and f[i][j] + 1 + b[i][j + 1] == lcs + 1:
                    seen.add(s2[j])
            ans += len(seen)

        return ans