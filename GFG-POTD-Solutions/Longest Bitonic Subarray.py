class Solution:
    def bitonic(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        inc = [1] * n
        dec = [1] * n

        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                inc[i] = inc[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1] + 1

        ans = 1
        for i in range(n):
            ans = max(ans, inc[i] + dec[i] - 1)

        return ans