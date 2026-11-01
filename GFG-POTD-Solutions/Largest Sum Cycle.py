class Solution:
    def largestSumCycle(self, edge):
        n = len(edge)
        visited = [False] * n
        max_sum = -1

        for i in range(n):
            if visited[i]:
                continue

            current = i
            path = {}
            path_sum = 0

            while current != -1 and not visited[current]:
                visited[current] = True
                path[current] = path_sum
                path_sum += current
                current = edge[current]

            if current != -1 and current in path:
                cycle_sum = 0
                node = current

                while True:
                    cycle_sum += node
                    node = edge[node]

                    if node == current:
                        break

                max_sum = max(max_sum, cycle_sum)

        return max_sum