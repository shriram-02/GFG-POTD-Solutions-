class Solution:

    def largestSubsquare(self, mat):
        n = len(mat)

        # Matrices to store count of 'X' to the right
        # and bottom of cells.
        right = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        # Fill the right and down matrices
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = 1 if j == n - 1 else right[i][j + 1] + 1
                    down[i][j] = 1 if i == n - 1 else down[i + 1][j] + 1

        maxSize = 0

        # Check each cell as the top-left
        # corner of the square
        for i in range(n):
            for j in range(n):

                # Calculate the maximum possible side
                # length for the square starting at (i, j)
                maxSide = min(right[i][j], down[i][j])

                # Iterate from the maximum side length down to 1
                for side in range(maxSide, 0, -1):

                    # Check if the square of length
                    # 'side' has valid borders
                    if right[i + side - 1][j] >= side and \
                    down[i][j + side - 1] >= side:
                        maxSize = max(maxSize, side)
                        break

        return maxSize
