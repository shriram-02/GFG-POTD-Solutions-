class Solution {
  public:
    int numberOfCells(int r, int c, int u, int d, vector<vector<char>> &mat) {
        int n = mat.size(), m = mat[0].size();

        if (mat[r][c] == '#') return 0;

        const int INF = 1e9;
        vector<vector<int>> dist(n, vector<int>(m, INF));
        deque<pair<int, int>> q;

        dist[r][c] = 0;
        q.push_front({r, c});

        int ans = 0;

        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        int cost[] = {1, 0, 0, 0};

        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop_front();

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m ||
                    mat[nx][ny] == '#')
                    continue;

                int nd = dist[x][y] + cost[k];

                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd;

                    if (cost[k] == 0)
                        q.push_front({nx, ny});
                    else
                        q.push_back({nx, ny});
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (mat[i][j] == '#') continue;

                int up = dist[i][j];
                if (up == INF) continue;

                int down = up + (i - r);

                if (up <= u && down <= d)
                    ans++;
            }
        }

        return ans;
    }
};