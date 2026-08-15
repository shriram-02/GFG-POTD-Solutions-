class Solution:

    def countWithout(self, n: int, d: int) -> int:
        if n <= 0:
            return 0

        s = str(n)
        length = len(s)

    # dp[tight][started] = count of valid completions from the current position onward
        dp = [[0] * 2 for _ in range(2)]

    # base case: at the end, a number counts only if it actually started (non-empty)
        for tight in range(2):
            for started in range(2):
                dp[tight][started] = started

    # build the table backward from the last digit position to the first
        for pos in range(length - 1, -1, -1):
            newDp = [[0] * 2 for _ in range(2)]

            for tight in range(2):
                for started in range(2):
                    limit = int(s[pos]) if tight else 9
                    total = 0

                # try every valid digit, skipping d once the number has started
                    for digit in range(0, limit + 1):
                        willStart = 1 if (started or digit != 0) else 0

                        if willStart and digit == d:
                            continue

                        newTight = 1 if (tight and digit == limit) else 0
                        total += dp[newTight][willStart]

                    newDp[tight][started] = total

            dp = newDp

        return dp[1][0]
