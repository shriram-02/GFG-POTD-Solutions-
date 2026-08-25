class Solution {
public:
    bool isNegativeWeightCycle(int V, vector<vector<int>>& edges) {
        vector<int> dist(V, 0); // initialize all distances to 0

        // Relax all edges V-1 times
        for (int i = 1; i <= V - 1; i++) {
            for (auto &edge : edges) {
                int u = edge[0], v = edge[1], w = edge[2];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        // Check for negative weight cycle
        for (auto &edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u] + w < dist[v]) {
                return true; // cycle found
            }
        }

        return false; // no cycle
    }
};
