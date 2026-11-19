class Solution:
    def sortIt(self, arr):
        odd = sorted([x for x in arr if x % 2 != 0], reverse=True)
        even = sorted([x for x in arr if x % 2 == 0])
        arr[:] = odd + even