''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # code here
        ans = float('-inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return float('inf')

            left_min = dfs(node.left)
            right_min = dfs(node.right)

            child_min = min(left_min, right_min)
            if child_min != float('inf'):
                ans = max(ans, node.data - child_min)

            return min(node.data, child_min)

        dfs(root)
        return ans