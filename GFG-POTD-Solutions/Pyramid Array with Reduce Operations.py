class Solution:

    def formPyramid(self, arr):
        n = len(arr)
        totalHeight = 0

        # Calculate the total height of all stones.
        for height in arr:
            totalHeight += height

        # For arrays of size 1 or 2, the only possible pyramid
        # has height 1, so the remaining stones must be reduced to 0.
        if n <= 2:
            return totalHeight - 1

        left = [0] * n
        right = [0] * n

        # left[i] = Maximum possible pyramid height at index i
        # considering only the left side.
        left[0] = 1
        for i in range(1, n):
            left[i] = min(left[i - 1] + 1, arr[i])

        # right[i] = Maximum possible pyramid height at index i
        # considering only the right side.
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1] + 1, arr[i])

        minCost = float('inf')

        # Try every index as the peak of the pyramid.
        for i in range(n):

            # The peak height is limited by both the left and right constraints.
            peakHeight = min(left[i], right[i])

            # A pyramid of height h has a total sum of h².
            pyramidSum = peakHeight * peakHeight

            # Cost = Original total height - Height of the constructed pyramid.
            minCost = min(minCost, totalHeight - pyramidSum)

        return minCost
