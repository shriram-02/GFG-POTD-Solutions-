class Solution:
    def maxIndexDifference(self, s):
        n = len(s)
        dp = [0] * n
        best = [-1] * 26
        ans = -1

        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')
            if c < 25 and best[c + 1] != -1:
                dp[i] = best[c + 1]
            else:
                dp[i] = i
            if dp[i] > best[c]:
                best[c] = dp[i]
            if c == 0:
                ans = max(ans, dp[i] - i)

        return ans