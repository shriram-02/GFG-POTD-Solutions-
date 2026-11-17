class Solution:
    def findPattern(self, s):
        balance = 0

        for ch in s:
            if ch == 'x':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

        return balance == 0