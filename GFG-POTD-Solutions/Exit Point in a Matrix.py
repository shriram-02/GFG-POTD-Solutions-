class Solution:
    def exitPoint(self, mat):
        n, m = len(mat), len(mat[0])

        dir = 0  # 0=right, 1=down, 2=left, 3=up
        i = j = 0

        while 0 <= i < n and 0 <= j < m:
            if mat[i][j] == 1:
                dir = (dir + 1) % 4
                mat[i][j] = 0

            if dir == 0:
                j += 1
            elif dir == 1:
                i += 1
            elif dir == 2:
                j -= 1
            else:
                i -= 1

        if dir == 0:
            j -= 1
        elif dir == 1:
            i -= 1
        elif dir == 2:
            j += 1
        else:
            i += 1

        return [i, j]