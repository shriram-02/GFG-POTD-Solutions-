class Solution {
public:
    int countSubsequences(string& s, int n) {
        const int MOD = 1e9 + 7;
        vector<long long> dp(n, 0);

        for (char c : s) {
            int d = c - '0';
            vector<long long> ndp = dp;

            ndp[d % n] = (ndp[d % n] + 1) % MOD;

            for (int r = 0; r < n; ++r) {
                int nr = (r * 10 + d) % n;
                ndp[nr] = (ndp[nr] + dp[r]) % MOD;
            }

            dp.swap(ndp);
        }

        return dp[0];
    }
};