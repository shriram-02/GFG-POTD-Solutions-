class Solution:
    def getCount(self, root, k):
        # code here
        if not root:
            return 0

        leaves = []
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()

            if not node.left and not node.right:
                leaves.append(level)
                continue

            if node.left:
                stack.append((node.left, level + 1))

            if node.right:
                stack.append((node.right, level + 1))

        leaves.sort()

        count = 0
        for cost in leaves:
            if cost > k:
                break
            k -= cost
            count += 1

        return count