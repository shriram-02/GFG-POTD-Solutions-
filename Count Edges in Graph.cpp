class Solution {
  public:
    int countEdges(vector<vector<int>> &adj) {
        int count = 0;
        for (int i = 0; i < adj.size(); i++) {
            count += adj[i].size();
        }
        return count / 2;
    }
};