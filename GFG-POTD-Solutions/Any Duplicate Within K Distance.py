class Solution:

    def checkWithinK(self, arr: list[int], k: int) -> bool:
        s = set()

        # Traverse the input array
        for i in range(len(arr)):

            # If already present in hash, then we found
            # a duplicate within k distance
            if arr[i] in s:
                return True

            # Add this item to hashset
            s.add(arr[i])

            # Remove the element that is now k+1 positions away
            if i >= k:
                s.remove(arr[i - k])

        return False
