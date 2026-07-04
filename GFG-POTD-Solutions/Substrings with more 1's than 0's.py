class Solution:
    def countSubstring(self, s):
        prefix = 0
        prefs = [0]
        for ch in s:
            prefix += 1 if ch == '1' else -1
            prefs.append(prefix)

        vals = sorted(set(prefs))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = [0] * (len(vals) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        for p in prefs:
            r = rank[p]
            ans += query(r - 1)
            update(r)

        return ans