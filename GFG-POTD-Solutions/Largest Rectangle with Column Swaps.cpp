class Solution {
public:
    int maxArea(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        
        // Step 1: Build heights matrix
        vector<vector<int>> height(n, vector<int>(m, 0));
        for (int j = 0; j < m; j++) {
            height[0][j] = mat[0][j];
            for (int i = 1; i < n; i++) {
                if (mat[i][j] == 1) {
                    height[i][j] = height[i-1][j] + 1;
                } else {
                    height[i][j] = 0;
                }
            }
        }
        
        int ans = 0;
        
        // Step 2: For each row, sort heights in descending order
        for (int i = 0; i < n; i++) {
            vector<int> row = height[i];
            sort(row.begin(), row.end(), greater<int>());
            
            // Step 3: Compute max area using sorted heights
            for (int j = 0; j < m; j++) {
                ans = max(ans, row[j] * (j + 1));
            }
        }
        
        return ans;
    }
};
