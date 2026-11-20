class Solution:
    def minFlips(self, s):
        count1 = 0
        count2 = 0

        for i in range(len(s)):
            if s[i] != str(i % 2):
                count1 += 1
            else:
                count2 += 1

        return min(count1, count2)