class Solution {
public:
    int minCost(int n, int i, int d, int c) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;

        for (int k = 1; k <= n; k++) {
            // Insert one character
            dp[k] = min(dp[k], dp[k - 1] + i);

            // If k is even, we can reach it by copy-paste from k/2
            if (k % 2 == 0) {
                dp[k] = min(dp[k], dp[k / 2] + c);
            } else {
                // If k is odd, we can reach it by copy-paste from (k+1)/2 and then delete
                dp[k] = min(dp[k], dp[(k + 1) / 2] + c + d);
            }
        }
        return dp[n];
    }
};
