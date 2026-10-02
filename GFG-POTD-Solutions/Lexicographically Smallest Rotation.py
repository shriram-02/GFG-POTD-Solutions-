class Solution:
    def lexiString(self, s: str) -> str:
        ss = s + s
        n = len(s)
        i, j, k = 0, 1, 0

        while i < n and j < n and k < n:
            if ss[i + k] == ss[j + k]:
                k += 1
                continue

            if ss[i + k] > ss[j + k]:
                i = i + k + 1
                if i <= j:
                    i = j + 1
            else:
                j = j + k + 1
                if j <= i:
                    j = i + 1

            k = 0

        start = min(i, j)
        return ss[start:start + n]