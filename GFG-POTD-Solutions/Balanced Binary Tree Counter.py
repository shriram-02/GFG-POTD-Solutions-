class Solution:
    def countBT(self, h: int) -> int:
        MOD = 10**9 + 7

        if h <= 1:
            return h

        a, b = 1, 3

        for i in range(3, h + 1):
            c = (b * (2 * a + b)) % MOD
            a, b = b, c

        return b