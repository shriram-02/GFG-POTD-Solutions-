class Solution:
    def findPosition(self, n):
        if n == 0 or (n & (n - 1)) != 0:
            return -1
        
        pos = 1
        while n > 1:
            n >>= 1
            pos += 1
        
        return pos