class Solution:
    def findSmallest(self, arr):
        arr.sort()
        
        res = 1
        
        for x in arr:
            if x > res:
                break
            
            res += x
        
        return res