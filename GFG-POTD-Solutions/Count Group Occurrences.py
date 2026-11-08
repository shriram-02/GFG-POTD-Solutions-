class Solution:
    def getCount(self, s, k):
        count = {}

        for i in range(len(s)):
            if i == 0 or s[i] != s[i - 1]:
                count[s[i]] = count.get(s[i], 0) + 1

        return sum(1 for v in count.values() if v == k)