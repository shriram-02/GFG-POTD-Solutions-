class Solution:
    def maxFrequency(self, arr, k):
        arr.sort()
        left = 0
        total = 0
        ans = 1

        for right in range(len(arr)):
            total += arr[right]

            while arr[right] * (right - left + 1) - total > k:
                total -= arr[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans