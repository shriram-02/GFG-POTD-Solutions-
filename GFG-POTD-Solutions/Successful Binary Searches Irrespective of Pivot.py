class Solution:
    def countAlwaysFound(self, arr):
        n = len(arr)
        left_max = [0] * n
        right_min = [float('inf')] * n

        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])

        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], arr[i + 1])

        count = 0
        for i in range(n):
            if arr[i] >= left_max[i] and arr[i] <= right_min[i]:
                count += 1

        return count