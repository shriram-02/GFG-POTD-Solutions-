class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        n = len(h)

        prev2 = 0
        prev1 = 0

        for i in range(n):
            curr = max(
                prev1,
                prev1 + l[i],
                prev2 + h[i]
            )
            prev2, prev1 = prev1, curr

        return prev1