class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        total = 0
        result = list(s)

        for i in range(len(roll) - 1, -1, -1):
            total = (total + 1) % 26
            roll[i] = min(roll[i], n)

        shifts = [0] * (n + 1)
        for r in roll:
            shifts[0] += 1
            shifts[r] -= 1

        curr = 0
        for i in range(n):
            curr += shifts[i]
            result[i] = chr((ord(s[i]) - ord('a') + curr) % 26 + ord('a'))

        return ''.join(result)