class Solution {
  public:
    int maxFruits(vector<int>& arr, int m) {
        int n = arr.size();
        m = min(m, n);

        long long sum = 0, ans = 0;

        for (int i = 0; i < m; i++)
            sum += arr[i];

        ans = sum;

        for (int i = m; i < n + m; i++) {
            sum += arr[i % n];
            sum -= arr[(i - m) % n];
            ans = max(ans, sum);
        }

        return (int)ans;
    }
};