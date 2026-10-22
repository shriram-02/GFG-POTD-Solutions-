class Solution:

    # Checks whether the given string can be converted into a palindrome.
    def isPossible(self, s):
        n = len(s)

        for i in range(n // 2):
            if s[i] != '?' and s[n - i - 1] != '?' and \
               s[i] != s[n - i - 1]:
                return False
        return True

    def minimumSum(self, s: str) -> int:
        if not self.isPossible(s):
            return -1

        s = list(s)
        n = len(s)

        # Copy known characters to their symmetric '?' positions.
        for i in range(n // 2):
            if s[i] == '?' and s[n - i - 1] != '?':
                s[i] = s[n - i - 1]
            elif s[i] != '?' and s[n - i - 1] == '?':
                s[n - i - 1] = s[i]

        st = []

        # Fill consecutive '?' using the nearest known character on the left.
        i = 0
        while i < n:
            if s[i] != '?':
                st.append(s[i])
                i += 1
            else:
                if st:
                    while i < n and s[i] == '?':
                        s[i] = st[-1]
                        i += 1
                    st.pop()
                else:
                    i += 1

        st.clear()

        # Fill remaining '?' using the nearest known character on the right.
        i = n - 1
        while i >= 0:
            if s[i] != '?':
                st.append(s[i])
                i -= 1
            else:
                if st:
                    while i >= 0 and s[i] == '?':
                        s[i] = st[-1]
                        i -= 1
                    st.pop()
                else:
                    i -= 1

        # If any '?' still remain, replace them with 'a'.
        for i in range(n):
            if s[i] == '?':
                s[i] = 'a'

        # Compute the sum of absolute differences of adjacent characters.
        ans = 0
        for i in range(n - 1):
            ans += abs((ord(s[i]) - ord('a')) - (ord(s[i + 1]) - ord('a')))

        return ans