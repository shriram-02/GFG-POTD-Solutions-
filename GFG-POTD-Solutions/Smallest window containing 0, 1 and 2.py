class Solution:
    def smallestSubstring(self, s):
        count = [0]*3
        left = 0
        res = float('inf')
        
        for right in range(len(s)):
            count[int(s[right])] += 1
            
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                res = min(res, right - left + 1)
                count[int(s[left])] -= 1
                left += 1
        
        return res if res != float('inf') else -1