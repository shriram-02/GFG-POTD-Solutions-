class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        window_sum = sum(arr[:totalTime])
        maximum = window_sum

        for i in range(totalTime, len(arr)):
            window_sum += arr[i] - arr[i - totalTime]
            maximum = max(maximum, window_sum)

        return maximum