import heapq

class Solution:
    def minComputation(self, files):
        heapq.heapify(files)
        cost = 0

        while len(files) > 1:
            x = heapq.heappop(files)
            y = heapq.heappop(files)
            merged = x + y
            cost += merged
            heapq.heappush(files, merged)

        return cost