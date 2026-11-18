class Solution:
    def findXOR(self, l: int, r: int) -> int:
        def xor(n):
            if n % 4 == 0:
                return n
            if n % 4 == 1:
                return 1
            if n % 4 == 2:
                return n + 1
            return 0

        return xor(r) ^ xor(l - 1)