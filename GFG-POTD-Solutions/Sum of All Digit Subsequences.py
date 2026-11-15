
class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        total = 0

        for digit in s:
            total = (total + int(digit) * pow(2, len(s) - 1, MOD)) % MOD

        return total
