class Solution:
    def minOperations(self, b):
        MOD = 10**9 + 7

        n = len(b)
        vis = [False] * n
        ans = 1

        def gcd(a, c):
            while c:
                a, c = c, a % c
            return a

        def lcm(a, c):
            return a // gcd(a, c) * c

        for i in range(n):
            if not vis[i]:
                cnt = 0
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = b[j] - 1
                    cnt += 1
                ans = lcm(ans, cnt) % MOD

        return ans