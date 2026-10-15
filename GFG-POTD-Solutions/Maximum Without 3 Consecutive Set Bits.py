class Solution:

    def maxValue(self, n: int) -> int:
        res = n

        # Find three consecutive set bits.
        for i in range(30, 1, -1):
            if (res & (1 << i)) and (res & (1 <<
                                            (i - 1))) and (res & (1 <<
                                                                  (i - 2))):

                # Clear the lowest bit of the three consecutive set bits.
                res &= ~(1 << (i - 2))

        return res
