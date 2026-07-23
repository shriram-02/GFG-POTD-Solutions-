class Solution:
    def canRepresentBST(self, arr):
        stack = []
        root = float('-inf')

        for val in arr:
            if val < root:
                return False

            while stack and val > stack[-1]:
                root = stack.pop()

            stack.append(val)

        return True