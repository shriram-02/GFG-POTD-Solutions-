class Solution {
public:
    bool isPossible(vector<int>& arr, int s, int x) {
        vector<long long> v;
        
        long long sum = s;
        v.push_back(s);

        for (int a : arr) {
            long long next = sum + a;
            
            // Numbers larger than x can never be part of the answer.
            if (next > x) break;
            
            v.push_back(next);
            sum += next;
        }

        // Even using all generated numbers, x cannot be formed.
        if (sum < x)
            return false;

        // Greedily choose the largest possible number.
        for (int i = (int)v.size() - 1; i >= 0; --i) {
            if (v[i] <= x)
                x -= v[i];
        }

        return x == 0;
    }
};