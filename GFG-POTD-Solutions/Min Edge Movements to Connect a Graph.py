class Solution:
    def minEdgesReq(self, n, edges):
        if len(edges) < n - 1:
            return -1

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return False
            if rank[a] < rank[b]:
                a, b = b, a
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1
            return True

        components = n

        for u, v in edges:
            if union(u, v):
                components -= 1

        return components - 1