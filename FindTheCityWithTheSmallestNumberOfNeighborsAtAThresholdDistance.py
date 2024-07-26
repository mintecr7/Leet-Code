from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph = [[-1] * n for _ in range(n)]
        for start, end, weight in edges:
            graph[start][end] = graph[end][start] = weight
        print(graph)
        return


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4

a = Solution()

ans = a.findTheCity(n, edges, distanceThreshold)
