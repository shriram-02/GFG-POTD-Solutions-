from bisect import bisect_right


class Solution:

    # Returns True if 'word' is a subsequence of string 's'
    def isSubsequence(self, word: str, pos: list) -> bool:

        prevIndex = -1

        for ch in word:

            # All positions where character 'ch' occurs in s
            indices = pos[ord(ch) - ord('a')]

            # Find first occurrence of ch after prevIndex
            idx = bisect_right(indices, prevIndex)

            # No valid next position found
            if idx == len(indices):
                return False

            # Update previously matched index
            prevIndex = indices[idx]

        return True

    def findLongestWord(self, s: str, d: list) -> str:

        # Store positions of every lowercase character in s
        pos = [[] for _ in range(26)]

        for i in range(len(s)):
            pos[ord(s[i]) - ord('a')].append(i)

        best = ""

        for word in d:

            # Skip smaller words directly
            if len(word) < len(best):
                continue

            # Check whether word is subsequence of s
            if self.isSubsequence(word, pos):

                # Prefer longer word
                # If same length, prefer lexicographically smaller word
                if (len(word) > len(best)
                        or (len(word) == len(best) and word < best)):

                    best = word

        return best
