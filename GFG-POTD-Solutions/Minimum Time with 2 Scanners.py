class Solution:

    def minTime(self, n: int, s1: int, s2: int) -> int:
        # Keep s1 as the smaller speed value.
        if s1 > s2:
            s1, s2 = s2, s1

        low: int = 0
        high: int = n
        minTime: int = s2 * n

        # Binary search over the number of tasks assigned to s1.
        while low <= high:
            mid: int = low + (high - low) // 2

            # Calculate the time taken by both workers.
            time1: int = mid * s1
            time2: int = (n - mid) * s2

            # Both workers work simultaneously, so take the maximum time.
            minTime = min(minTime, max(time1, time2))

            # Move towards a more balanced distribution of work.
            if time1 <= time2:
                low = mid + 1
            else:
                high = mid - 1

        return minTime
