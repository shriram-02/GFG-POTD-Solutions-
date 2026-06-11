class Solution:
    def findIndex(self, s):
        total_close = s.count(')')
        open_count = 0
        close_remaining = total_close

        for i in range(len(s)):
            if open_count == close_remaining:
                return i

            if s[i] == '(':
                open_count += 1
            else:
                close_remaining -= 1

        return len(s)