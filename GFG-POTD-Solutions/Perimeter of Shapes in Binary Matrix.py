class Solution:
    def findPerimeter(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        perimeter = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    perimeter += 4

                    if i > 0 and mat[i - 1][j] == 1:
                        perimeter -= 2

                    if j > 0 and mat[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter