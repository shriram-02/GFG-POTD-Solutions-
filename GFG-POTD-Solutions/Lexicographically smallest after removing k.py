class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)

        if n & (n - 1) == 0:
            k //= 2
        else:
            k *= 2

        if k <= 0:
            return s

        if k >= n:
            return -1

        stack = []
        rem = k

        for ch in s:
            while rem > 0 and stack and stack[-1] > ch:
                stack.pop()
                rem -= 1
            stack.append(ch)

        while rem > 0:
            stack.pop()
            rem -= 1

        ans = ''.join(stack)
        return ans if ans else -1