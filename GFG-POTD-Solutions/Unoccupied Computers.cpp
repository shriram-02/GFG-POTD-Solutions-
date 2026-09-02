class Solution {
  public:
    int solve(int n, string s) {
        unordered_set<char> inside;
        unordered_set<char> rejected;
        int ans = 0;

        for (char c : s) {
            if (inside.count(c)) {
                inside.erase(c);
            } 
            else if (rejected.count(c)) {
                rejected.erase(c);
            } 
            else {
                if ((int)inside.size() < n) {
                    inside.insert(c);
                } else {
                    rejected.insert(c);
                    ans++;
                }
            }
        }

        return ans;
    }
};