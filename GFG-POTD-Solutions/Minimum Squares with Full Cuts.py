class Solution:
    def minSquares(self, n, m):
        count = 0
        while n and m:
            if n < m:
                n, m = m, n
            count += n // m
            n %= m
        return count