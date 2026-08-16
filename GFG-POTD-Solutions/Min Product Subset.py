ans = float('inf')
            n = len(arr)

            for mask in range(1, 1 << n):
                prod = 1
                for i in range(n):
                    if mask & (1 << i):
                        prod *= arr[i]
                ans = min(ans, prod)

            return ans