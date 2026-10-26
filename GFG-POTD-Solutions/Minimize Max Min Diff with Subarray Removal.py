class Solution:

    def minDiff(self, k: int, arr: list[int]) -> int:

        n = len(arr)

        # Maximum and minimum values from each index to the end.
        suffixMax = [0] * n
        suffixMin = [0] * n

        suffixMax[-1] = arr[-1]
        suffixMin[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(arr[i], suffixMax[i + 1])
            suffixMin[i] = min(arr[i], suffixMin[i + 1])

        # Remove the prefix of size k.
        ans = suffixMax[k] - suffixMin[k]

        prefixMax = arr[0]
        prefixMin = arr[0]

        # Remove a middle subarray of size k.
        for i in range(1, n - k):

            currentMax = max(prefixMax, suffixMax[i + k])
            currentMin = min(prefixMin, suffixMin[i + k])

            ans = min(ans, currentMax - currentMin)

            prefixMax = max(prefixMax, arr[i])
            prefixMin = min(prefixMin, arr[i])

        # Remove the suffix of size k.
        ans = min(ans, prefixMax - prefixMin)

        return ans
