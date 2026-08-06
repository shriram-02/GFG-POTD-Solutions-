class Solution:
    def countMinOperations(self, arr):
        inc = 0
        dbl = 0

        for x in arr:
            inc += x.bit_count()
            if x:
                dbl = max(dbl, x.bit_length() - 1)

        return inc + dbl