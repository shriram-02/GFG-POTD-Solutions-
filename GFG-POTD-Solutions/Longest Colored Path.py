from collections import defaultdict


class Solution:

    def root(self, adj, s, sa, node=0, par=-1):
        ra, ba = 0, 0  # ra: max red path, ba: max blue path
        for it in adj[node]:
            if it == par:
                continue
            self.root(adj, s, sa, it, node)
            ra = max(ra, sa[it][0])
            ra = max(ra, sa[it][1])
            ba = max(ba, sa[it][1])

        if s[node] == 'R':
            sa[node][0] = ra + 1
            sa[node][1] = 0
        else:
            sa[node][0] = ba + 1
            sa[node][1] = ba + 1

    def reroot(self, adj, s, ans, sa, node=0, par=-1, red_par=0, blue_par=0):
        if s[node] == 'R':
            ans[node][0] = max(sa[node][0], 1 + red_par)
            ans[node][1] = 0
        else:
            ans[node][0] = max(sa[node][0], 1 + blue_par)
            ans[node][1] = max(sa[node][1], 1 + blue_par)

        fr, sr = red_par, red_par
        fb, sb = blue_par, blue_par

        for it in adj[node]:
            if it == par:
                continue
            if sa[it][0] > fr:
                sr = fr
                fr = sa[it][0]
            elif sa[it][0] > sr:
                sr = sa[it][0]

            if sa[it][1] > fb:
                sb = fb
                fb = sa[it][1]
            elif sa[it][1] > sb:
                sb = sa[it][1]

        for it in adj[node]:
            if it == par:
                continue

            new_red = 1
            new_blue = 0

            if s[node] == 'R':
                if sa[it][0] == fr:
                    new_red += sr
                else:
                    new_red += fr
            else:
                if sa[it][1] == fb:
                    new_red += sb
                else:
                    new_red += fb
                new_blue = new_red

            self.reroot(adj, s, ans, sa, it, node, new_red, new_blue)

    def longestPath(self, s, edges):
        n = len(s)
        adj = defaultdict(list)

        for u, v in edges:
            adj[u - 1].append(v - 1)  # Convert to 0-indexed
            adj[v - 1].append(u - 1)  # Convert to 0-indexed

        # 0 - represent red, 1 - represent blue
        subTreeAns = [[0, 0] for _ in range(n)]
        self.root(adj, s, subTreeAns)

        ans = [[0, 0] for _ in range(n)]
        self.reroot(adj, s, ans, subTreeAns)

        res = 0
        for i in range(n):
            res = max(res, ans[i][0], ans[i][1])

        return res
