class Solution {
  public:
    int palindromicStrings(int n, int k) {
        int MOD = 1e9 + 7;

        long long nPr[k + 1][k + 1];

        memset(nPr, 0, sizeof nPr);

        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= i; j++) {
                // Base Cases
                if (j == 0)
                    nPr[i][j] = 1;

                // Calculate value using
                // previosly stored values
                else
                    nPr[i][j] =
                        (nPr[i - 1][j] % MOD + (j * nPr[i - 1][j - 1]) % MOD) % MOD;
            }
        }

        long long ans = 0;

        for (int i = 1; i <= n / 2; i++)
            ans = (ans + nPr[k][i]) % MOD;

        ans = (ans * 2) % MOD;

        if (n & 1)
            ans = (ans + nPr[k][n / 2 + 1]) % MOD;

        return (int)ans;
    }
};