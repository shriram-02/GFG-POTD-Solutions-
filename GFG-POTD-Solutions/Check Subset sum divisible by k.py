class Solution:
    def divisibleByK(self, arr, k):
        dp = [False] * k

        for x in arr:
            x %= k
            new_dp = dp[:]
            new_dp[x] = True
            for r in range(k):
                if dp[r]:
                    new_dp[(r + x) % k] = True
            dp = new_dp
            if dp[0]:
                return True

        return False