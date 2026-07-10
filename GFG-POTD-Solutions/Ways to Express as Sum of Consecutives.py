class Solution:
    def getCount(self, n):
        while n % 2 == 0:
            n //= 2

        ans = 1
        p = 3
        while p * p <= n:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            ans *= (cnt + 1)
            p += 2

        if n > 1:
            ans *= 2

        return ans - 1