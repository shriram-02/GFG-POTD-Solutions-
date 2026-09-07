class Solution {
public:
    int n;
    vector<int> a;
    int dp[101][102][102];

    int solve(int i, int inc, int dec) {
        if (i == n) return 0;

        int &res = dp[i][inc][dec];
        if (res != -1) return res;

        res = 1 + solve(i + 1, inc, dec);

        if (inc == n || a[i] > a[inc])
            res = min(res, solve(i + 1, i, dec));

        if (dec == n || a[i] < a[dec])
            res = min(res, solve(i + 1, inc, i));

        return res;
    }

    int minCount(vector<int>& arr) {
        a = arr;
        n = a.size();
        memset(dp, -1, sizeof(dp));
        return solve(0, n, n);
    }
};