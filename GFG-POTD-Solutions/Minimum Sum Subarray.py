
class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        curr = ans = arr[0]

        for num in arr[1:]:
            curr = min(num, curr + num)
            ans = min(ans, curr)

        return ans
