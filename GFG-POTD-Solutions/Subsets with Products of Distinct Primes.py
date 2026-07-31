class Solution:
    def countSubsets(self, arr):
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        freq = [0] * 31
        for x in arr:
            freq[x] += 1

        masks = [-1] * 31
        for x in range(2, 31):
            t = x
            mask = 0
            ok = True
            for i, p in enumerate(primes):
                if t % p == 0:
                    if t % (p * p) == 0:
                        ok = False
                        break
                    mask |= (1 << i)
            if ok:
                masks[x] = mask

        dp = [0] * (1 << 10)
        dp[0] = 1

        for v in range(2, 31):
            if freq[v] == 0 or masks[v] == -1:
                continue
            m = masks[v]
            ndp = dp[:]
            for mask in range(1 << 10):
                if (mask & m) == 0:
                    ndp[mask | m] = (ndp[mask | m] + dp[mask] * freq[v]) % MOD
            dp = ndp

        ways_one = pow(2, freq[1], MOD)
        ans = (sum(dp) - dp[0]) % MOD
        ans = (ans * ways_one) % MOD
        return ans