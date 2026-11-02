
class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return 0

            count = size[ra] * size[rb]

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

            return count

        edges.sort(key=lambda x: x[2])

        sorted_queries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        ans = [0] * len(queries)
        total = 0
        j = 0

        for weight, idx in sorted_queries:
            while j < len(edges) and edges[j][2] <= weight:
                u, v, w = edges[j]
                total += union(u, v)
                j += 1

            ans[idx] = total

        return ans
