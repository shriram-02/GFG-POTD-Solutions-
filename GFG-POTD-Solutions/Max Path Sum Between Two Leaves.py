'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def maxPathSum(self, root):
        if root is None:
            return -1

        ans = [float('-inf')]

        def dfs(node):
            if node is None:
                return float('-inf')

            if node.left is None and node.right is None:
                return node.data

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left is not None and node.right is not None:
                ans[0] = max(ans[0], left + node.data + right)
                return max(left, right) + node.data

            if node.left is not None:
                return left + node.data

            return right + node.data

        dfs(root)

        return ans[0] if ans[0] != float('-inf') else -1