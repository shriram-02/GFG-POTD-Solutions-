class Solution:
    def minToggle(self, arr):
        n = len(arr)
        
        prefix_ones = [0] * (n + 1)
        suffix_zeros = [0] * (n + 1)
        
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + (arr[i] == 1)
        
        for i in range(n - 1, -1, -1):
            suffix_zeros[i] = suffix_zeros[i + 1] + (arr[i] == 0)
        
        ans = n
        
        for i in range(n + 1):
            ans = min(ans, prefix_ones[i] + suffix_zeros[i])
        
        return ans