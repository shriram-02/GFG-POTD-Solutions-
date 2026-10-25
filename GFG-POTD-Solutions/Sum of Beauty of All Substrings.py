class Solution:

    def beautySum(self, s: str) -> int:
        ans = 0

        # Fix the starting index of the substring.
        for i in range(len(s)):
            cnt = [0] * 26
            max_f = 0

            # Extend the substring one character at a time.
            for j in range(i, len(s)):
                idx = ord(s[j]) - 97
                cnt[idx] += 1
                max_f = max(max_f, cnt[idx])

                min_f = len(s) + 1

                # Find the minimum non-zero frequency.
                for freq in cnt:
                    if freq > 0:
                        min_f = min(min_f, freq)

                # Add the beauty of the current substring.
                ans += max_f - min_f

        return ans
