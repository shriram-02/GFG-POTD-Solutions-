arr.sort()

        def count_at_most(target):
            n = len(arr)
            count = 0

            for i in range(n - 2):
                left = i + 1
                right = n - 1

                while left < right:
                    total = arr[i] + arr[left] + arr[right]

                    if total <= target:
                        # Every pair from left to right-1
                        # with arr[i] has sum <= target.
                        count += right - left
                        left += 1
                    else:
                        right -= 1

            return count

        return count_at_most(r) - count_at_most(l - 1)