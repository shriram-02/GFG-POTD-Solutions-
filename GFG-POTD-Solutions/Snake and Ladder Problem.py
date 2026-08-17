 N = n * n
        jump = [0] * (N + 1)

        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]

        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]

        from collections import deque

        dist = [-1] * (N + 1)
        q = deque([1])
        dist[1] = 0

        while q:
            cur = q.popleft()

            if cur == N:
                return dist[cur]

            for dice in range(1, 7):
                nxt = cur + dice

                if nxt > N:
                    break

                if jump[nxt]:
                    nxt = jump[nxt]

                if dist[nxt] == -1:
                    dist[nxt] = dist[cur] + 1
                    q.append(nxt)
