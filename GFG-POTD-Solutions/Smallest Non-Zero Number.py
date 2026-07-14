class Solution:
    def find(self, arr):
        req = 0
        for a in reversed(arr):
            req = (req + a + 1) // 2
        return max(1, req)