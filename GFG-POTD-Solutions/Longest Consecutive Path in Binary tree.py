class Solution:
    def longestConsecutive(self, root):
        self.ans = 1

        def dfs(node, prev, length):
            if not node:
                return

            if prev is not None and node.data == prev + 1:
                length += 1
            else:
                length = 1

            self.ans = max(self.ans, length)

            dfs(node.left, node.data, length)
            dfs(node.right, node.data, length)

        dfs(root, None, 0)
        return self.ans if self.ans > 1 else -1