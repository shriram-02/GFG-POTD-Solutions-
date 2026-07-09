class Solution:
    def countKdivPairs(self, arr, k):
        freq = [0] * k
        count = 0

        for num in arr:
            rem = num % k
            comp = (k - rem) % k
            count += freq[comp]
            freq[rem] += 1

        return count