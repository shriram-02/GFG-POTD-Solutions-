class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        s1, s2 = [], []
        ans = []

        while r1 or r2 or s1 or s2:
            while r1:
                s1.append(r1)
                r1 = r1.left

            while r2:
                s2.append(r2)
                r2 = r2.left

            if s1 and s2:
                if s1[-1].data == s2[-1].data:
                    ans.append(s1[-1].data)
                    r1 = s1.pop().right
                    r2 = s2.pop().right
                elif s1[-1].data < s2[-1].data:
                    r1 = s1.pop().right
                else:
                    r2 = s2.pop().right
            elif s1:
                r1 = s1.pop().right
            elif s2:
                r2 = s2.pop().right

        return ans