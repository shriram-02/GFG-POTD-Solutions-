class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr) // 2
        first = sorted(arr[:n])
        second = sorted(arr[n:])
        
        ans = 0
        j = 0
        
        for x in first:
            while j < n and x >= 5 * second[j]:
                j += 1
            ans += j
        
        return ans