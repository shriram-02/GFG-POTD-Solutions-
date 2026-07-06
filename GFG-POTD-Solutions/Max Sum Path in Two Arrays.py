class Solution:
    def maxPathSum(self, a, b):
        i = j = 0
        s1 = s2 = ans = 0
        n, m = len(a), len(b)

        while i < n and j < m:
            if a[i] < b[j]:
                s1 += a[i]
                i += 1
            elif a[i] > b[j]:
                s2 += b[j]
                j += 1
            else:
                ans += max(s1, s2) + a[i]
                s1 = s2 = 0
                i += 1
                j += 1

        while i < n:
            s1 += a[i]
            i += 1

        while j < m:
            s2 += b[j]
            j += 1

        ans += max(s1, s2)
        return ans