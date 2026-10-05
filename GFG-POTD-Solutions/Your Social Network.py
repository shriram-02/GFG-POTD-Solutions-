class Solution:

    def socialNetwork(self, arr):
        n = len(arr) + 1

        # Store all reachable connections.
        ans = []

        # Process users from 2 to n.
        for i in range(2, n + 1):

            # Store the friend chain of user i.
            path = []

            curr = i

            # Follow the friend chain until user 1.
            while curr != 1:
                curr = arr[curr - 2]

                # Store the reachable user.
                path.append(curr)

            # Process the path in reverse so that
            # users j are considered in increasing order.
            distance = len(path)

            for j in range(len(path) - 1, -1, -1):

                # Distance from i to path[j].
                ans.append([i, path[j], distance])

                distance -= 1

        return ans
