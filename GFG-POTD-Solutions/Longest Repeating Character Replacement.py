class Solution:
    def longestSubstr(self, s, k):
        # Code here
        freq = [0]*26
        left = 0
        max_freq = 0 
        res = 0
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            freq[idx] += 1
            max_freq = max(max_freq,freq[idx])
            
            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            res = max(res,right-left + 1)
        return res