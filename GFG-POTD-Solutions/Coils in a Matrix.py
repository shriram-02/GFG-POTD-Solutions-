class Solution:

    def formCoils(self, n: int) -> list[list[int]]:

        # Number of elements in each coil
        m = 8 * n * n

        # Let us fill elements in coil1.
        coil1 = [0] * m

        # First element of coil1
        coil1[0] = 8 * n * n + 2 * n
        curr = coil1[0]

        nflg = 1
        step = 2

        # Fill remaining elements in coil1
        index = 1
        while index < m:

            # Fill elements of current step from down to up
            for _ in range(step):
                curr -= 4 * n * nflg
                coil1[index] = curr
                index += 1
                if index >= m:
                    break

            if index >= m:
                break

            # Fill elements of current step from up to down
            for _ in range(step):
                curr += nflg
                coil1[index] = curr
                index += 1
                if index >= m:
                    break

            nflg = -nflg
            step += 2

        # Get coil2 from coil1
        coil2 = [16 * n * n + 1 - x for x in coil1]

        coil2.reverse()
        coil1.reverse()

        return [coil2, coil1]
