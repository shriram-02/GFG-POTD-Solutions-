class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)

        # Step 1: Compute max subarray sum ending at each index (Kadane’s)
        max_end_here = [0] * n
        max_end_here[0] = arr[0]
        for i in range(1, n):
            max_end_here[i] = max(arr[i], max_end_here[i-1] + arr[i])

        # Step 2: Compute sum of first k elements
        window_sum = sum(arr[:k])
        result = window_sum

        # Step 3: Slide the window and check max sum with extension
        for i in range(k, n):
            window_sum += arr[i] - arr[i-k]
            result = max(result, window_sum)
            result = max(result, window_sum + max_end_here[i-k])

        return result
