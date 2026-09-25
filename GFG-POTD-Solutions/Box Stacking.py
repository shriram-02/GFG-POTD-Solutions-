class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        boxes = []

        for i in range(len(height)):
            a, b, c = height[i], width[i], length[i]
            boxes.append((max(a, b), min(a, b), c))
            boxes.append((max(b, c), min(b, c), a))
            boxes.append((max(a, c), min(a, c), b))

        boxes.sort(reverse=True)

        n = len(boxes)
        dp = [0] * n

        ans = 0

        for i in range(n):
            dp[i] = boxes[i][2]

            for j in range(i):
                if boxes[j][0] > boxes[i][0] and boxes[j][1] > boxes[i][1]:
                    dp[i] = max(dp[i], dp[j] + boxes[i][2])

            ans = max(ans, dp[i])

        return ans