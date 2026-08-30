class Solution {
  public:

    // Finds the interval containing the given rank
    int findInterval(vector<int> &prefix, int low, int high, int rank) {
        while (low < high) {
            int mid = low + (high - low) / 2;

            if (prefix[mid] < rank)
                low = mid + 1;
            else
                high = mid;
        }

        return low;
    }

    vector<int> getMarks(vector<int> &l, vector<int> &r, vector<int> &rank) {
        int n = l.size();

        // Stores the cumulative number of marks till each interval
        vector<int> prefix(n);
        prefix[0] = r[0] - l[0] + 1;

        for (int i = 1; i < n; i++)
            prefix[i] = prefix[i - 1] + (r[i] - l[i] + 1);

        vector<int> ans(rank.size());

        for (int i = 0; i < rank.size(); i++) {

            // Find the interval containing the required rank
            int idx = findInterval(prefix, 0, n - 1, rank[i]);

            // Compute the corresponding mark
            int diff = prefix[idx] - rank[i];
            ans[i] = r[idx] - diff;
        }

        return ans;
    }
};