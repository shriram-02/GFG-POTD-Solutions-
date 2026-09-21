class Solution:

    def areAnagrams(self, root1, root2):
        from collections import Counter, deque

        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            n1 = len(q1)
            n2 = len(q2)

            if n1 != n2:
                return False

            level1 = []
            level2 = []

            for _ in range(n1):
                node = q1.popleft()
                level1.append(node.data)

                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)

            for _ in range(n2):
                node = q2.popleft()
                level2.append(node.data)

                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            if Counter(level1) != Counter(level2):
                return False

        return not q1 and not q2