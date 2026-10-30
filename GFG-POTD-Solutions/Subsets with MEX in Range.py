class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        M = 1000000007
        n = len(arr)

        mp = {}
        for num in arr:
            mp[num] = mp.get(num, 0) + 1

        # Precompute powers of 2 modulo M.
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 2) % M

        res = 0
        cur = 1
        seen = 0

        # Ensure every value smaller than l is present.
        for i in range(l):
            freq = mp.get(i, 0)

            if freq == 0:
                return 0

            seen += freq
            cur = (cur * (power[freq] - 1 + M)) % M

        # Count subsets for each possible MEX.
        for i in range(l, r + 1):
            freq = mp.get(i, 0)

            here = (cur * power[n - seen - freq]) % M
            res = (res + here) % M

            # No larger MEX is possible if i is absent.
            if freq == 0:
                return res

            seen += freq
            cur = (cur * (power[freq] - 1 + M)) % M

        return res
