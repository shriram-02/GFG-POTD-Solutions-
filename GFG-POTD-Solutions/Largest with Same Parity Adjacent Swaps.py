class Solution:

    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        n = len(arr)
        i = 0

        # Process each maximal contiguous subarray having the same parity.
        while i < n:
            j = i + 1

            while j < n and (arr[j] + arr[j - 1]) % 2 == 0:
                j += 1

            # Sort the current subarray in descending order.
            arr[i:j] = sorted(arr[i:j], reverse=True)

            i = j

        return arr