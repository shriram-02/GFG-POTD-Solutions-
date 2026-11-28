class Solution {
  public:
    bool checkPath(vector<vector<int>> &adj, int u, int v) {
        int n = adj.size();
        vector<bool> visited(n, false);
        queue<int> q;

        visited[u] = true;
        q.push(u);

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            if (node == v)
                return true;

            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        return false;
    }
};