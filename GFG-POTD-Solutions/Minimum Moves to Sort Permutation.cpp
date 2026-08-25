class Solution {
public:
    int minMoves(vector<int>& arr) {
        int n = arr.size();
        vector<int> pos(n+1);
        
        // store positions of each number
        for(int i=0;i<n;i++) {
            pos[arr[i]] = i;
        }
        
        // find longest increasing subsequence in terms of positions
        int longest = 1, curr = 1;
        for(int i=2;i<=n;i++) {
            if(pos[i] > pos[i-1]) {
                curr++;
                longest = max(longest, curr);
            } else {
                curr = 1;
            }
        }
        
        return n - longest;
    }
};
