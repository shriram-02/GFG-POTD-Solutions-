'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        n = len(pre)
        pos = {v: i for i, v in enumerate(preMirror)}
        self.preIndex = 0

        def build(l, h):
            if self.preIndex >= n or l > h:
                return None

            root = Node(pre[self.preIndex])
            self.preIndex += 1

            if l == h or self.preIndex >= n:
                return root

            idx = pos[pre[self.preIndex]]

            root.left = build(idx, h)
            root.right = build(l + 1, idx - 1)

            return root

        return build(0, n - 1)