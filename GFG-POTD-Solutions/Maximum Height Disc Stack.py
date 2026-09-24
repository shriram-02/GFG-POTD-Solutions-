class Solution:

    def query(self, bit, idx):
        res = 0

        # Find the maximum stack height for smaller compressed heights.
        while idx > 0:
            res = max(res, bit[idx])
            idx -= idx & -idx

        return res

    def update(self, bit, idx, val):
        n = len(bit)

        # Update Fenwick tree nodes with the maximum stack height.
        while idx < n:
            bit[idx] = max(bit[idx], val)
            idx += idx & -idx

    def maxStackHeight(self, r, h):
        n = len(r)
        discs = []

        # Store each disc as a radius-height pair.
        for i in range(n):
            discs.append((r[i], h[i]))

        discs.sort()

        # Compress heights for Fenwick tree indexing.
        heights = sorted(set(h))

        bit = [0] * (len(heights) + 1)
        res = 0

        # Process equal-radius discs together to maintain strict radius ordering.
        i = 0

        while i < n:
            j = i
            updates = []

            # Compute values before applying updates from the current radius group.
            while j < n and discs[j][0] == discs[i][0]:
                height = discs[j][1]
                idx = self.lower_bound(heights, height) + 1

                cur = height + self.query(bit, idx - 1)
                updates.append((idx, cur))
                res = max(res, cur)
                j += 1

            # Apply updates after processing all discs with the same radius.
            for idx, val in updates:
                self.update(bit, idx, val)

            i = j

        return res

    def lower_bound(self, arr, val):
        left = 0
        right = len(arr)

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < val:
                left = mid + 1
            else:
                right = mid

        return left
