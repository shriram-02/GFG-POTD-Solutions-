class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        from math import gcd

        n = len(arr)
        size = 1
        while size < n:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(n):
            tree[size + i] = arr[i]

        for i in range(size - 1, 0, -1):
            tree[i] = gcd(tree[2 * i], tree[2 * i + 1])

        def update(index, value):
            pos = size + index
            tree[pos] = value
            pos //= 2

            while pos:
                tree[pos] = gcd(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def query(left, right):
            left += size
            right += size
            result = 0

            while left <= right:
                if left & 1:
                    result = gcd(result, tree[left])
                    left += 1

                if not (right & 1):
                    result = gcd(result, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return result

        ans = []

        for query_data in queries:
            if query_data[0] == 0:
                _, l, r = query_data
                ans.append(query(l, r))
            else:
                _, index, value = query_data
                update(index, value)

        return ans