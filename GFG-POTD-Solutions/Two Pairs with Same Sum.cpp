class Solution {
  public:
    vector<int> findPairs(vector<int>& arr) {
        int n = arr.size();

        unordered_map<int, pair<int, int>> mp;
        vector<int> res;

        // Generate pairs in lexicographical order.
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int sum = arr[i] + arr[j];

                // Store the first pair for this sum.
                if (mp.find(sum) == mp.end()) {
                    mp[sum] = {i, j};
                    continue;
                }

                int a = mp[sum].first;
                int b = mp[sum].second;

                // Ensure all four indices are distinct.
                if (a == i || a == j || b == i || b == j)
                    continue;

                vector<int> cur = {a, b, i, j};

                // Keep the lexicographically smallest quadruplet.
                if (res.empty() || cur < res)
                    res = cur;
            }
        }

        if (res.empty())
            return {-1, -1, -1, -1};

        return res;
    }
};