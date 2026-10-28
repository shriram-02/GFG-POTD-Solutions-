class Solution:
    def nthCharacter(self, n):
        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // length
        index = (n - 1) % length

        return str(num)[index]