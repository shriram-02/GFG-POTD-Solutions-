class Solution:

    def update(self, n: int, updates: list[int]) -> list[int]:
        arr = [0] * n

        # Count the number of updates starting at each position
        for j in updates:
            arr[j - 1] += 1

        # Build the final array using prefix sum
        count = 0

        for i in range(n):
            count += arr[i]
            arr[i] = count

        return arr
