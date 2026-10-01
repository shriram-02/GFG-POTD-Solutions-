class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in dependencies:
            adj[u].append(v)
            indegree[v] += 1

        from collections import deque
        q = deque()
        dp = [0] * n

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = duration[i]

        count = 0
        ans = 0

        while q:
            u = q.popleft()
            count += 1
            ans = max(ans, dp[u])

            for v in adj[u]:
                dp[v] = max(dp[v], dp[u] + duration[v])
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        return -1 if count != n else ans