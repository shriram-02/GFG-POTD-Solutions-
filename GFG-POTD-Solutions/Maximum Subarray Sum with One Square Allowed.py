class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        no_square = arr[0]
        one_square = arr[0] ** 2
        ans = one_square

        for i in range(1, len(arr)):
            x = arr[i]

            one_square = max(
                one_square + x,
                no_square + x * x,
                x * x
            )

            no_square = max(no_square + x, x)

            ans = max(ans, no_square, one_square)

        return ans