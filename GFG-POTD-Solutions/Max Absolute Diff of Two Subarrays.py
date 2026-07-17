class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)

        leftMax = [0] * n
        leftMin = [0] * n
        rightMax = [0] * n
        rightMin = [0] * n

        cur = best = arr[0]
        leftMax[0] = best
        for i in range(1, n):
            cur = max(arr[i], cur + arr[i])
            best = max(best, cur)
            leftMax[i] = best

        cur = best = arr[0]
        leftMin[0] = best
        for i in range(1, n):
            cur = min(arr[i], cur + arr[i])
            best = min(best, cur)
            leftMin[i] = best

        cur = best = arr[-1]
        rightMax[-1] = best
        for i in range(n - 2, -1, -1):
            cur = max(arr[i], cur + arr[i])
            best = max(best, cur)
            rightMax[i] = best

        cur = best = arr[-1]
        rightMin[-1] = best
        for i in range(n - 2, -1, -1):
            cur = min(arr[i], cur + arr[i])
            best = min(best, cur)
            rightMin[i] = best

        ans = 0
        for i in range(n - 1):
            ans = max(
                ans,
                abs(leftMax[i] - rightMin[i + 1]),
                abs(leftMin[i] - rightMax[i + 1])
            )

        return ans