from bisect import bisect_left

class Solution:
    def minDeletions(self, arr):
        lis = []
        for x in arr:
            i = bisect_left(lis, x)
            if i == len(lis):
                lis.append(x)
            else:
                lis[i] = x
        return len(arr) - len(lis)