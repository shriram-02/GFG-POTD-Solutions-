import heapq

class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7

        heap = [-x for x in arr]
        heapq.heapify(heap)

        ans = 0
        while k > 0 and heap:
            x = -heapq.heappop(heap)
            ans = (ans + x) % MOD
            if x > 1:
                heapq.heappush(heap, -(x - 1))
            k -= 1

        return ans