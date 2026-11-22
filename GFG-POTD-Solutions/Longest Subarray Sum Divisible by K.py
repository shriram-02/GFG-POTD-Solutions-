class Solution:
    def longestSubarrayDivK(self, arr, k):
        prefix_sum = 0
        first_occurrence = {0: -1}
        max_length = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]
            remainder = prefix_sum % k

            if remainder in first_occurrence:
                max_length = max(max_length, i - first_occurrence[remainder])
            else:
                first_occurrence[remainder] = i

        return max_length