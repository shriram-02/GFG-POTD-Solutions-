class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        stack = []
        
        for x in arr:
            if stack and ((stack[-1] >= 0 and x < 0) or (stack[-1] < 0 and x >= 0)):
                stack.pop()
            else:
                stack.append(x)
        
        return stack