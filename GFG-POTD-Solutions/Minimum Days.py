
class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        n = len(s)

        def check(days):
            removed = [False] * n

            for i in range(days):
                removed[p[i]] = True

            for i in range(n - 1):
                if not removed[i] and not removed[i + 1]:
                    if s[i] == s[i + 1]:
                        return False

            return True

        low, high = 0, n

        while low < high:
            mid = (low + high) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low
