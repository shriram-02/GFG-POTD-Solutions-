class Solution:
    def levelSort(self, arr):
        res = []
        i = 0
        level = 0
        n = len(arr)
        
        while i < n:
            cnt = min(1 << level, n - i)
            curr = arr[i:i + cnt]
            curr.sort()
            res.append(curr)
            i += cnt
            level += 1
            
        return res