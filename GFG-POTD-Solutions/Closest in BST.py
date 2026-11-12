class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        min_diff = float('inf')
        curr = root
        
        while curr:
            min_diff = min(min_diff, abs(curr.data - k))
            
            if curr.data == k:
                return 0
            elif k < curr.data:
                curr = curr.left
            else:
                curr = curr.right
                
        return min_diff