class Solution:
    def subarrayXor(self, arr):
        n = len(arr)

        if n % 2 == 0:
            return 0

        result = 0
        for i in range(0, n, 2):
            result ^= arr[i]

        return result