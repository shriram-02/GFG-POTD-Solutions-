from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def freqInRange(self, arr, queries):
        pos = defaultdict(list)

        for i, val in enumerate(arr):
            pos[val].append(i)

        ans = []
        for l, r, x in queries:
            indices = pos.get(x, [])
            ans.append(bisect_right(indices, r) - bisect_left(indices, l))

        return ans