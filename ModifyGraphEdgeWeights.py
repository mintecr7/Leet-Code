from typing import List


class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        return []


n = 5
target = 5
source = 0
destination = 1
edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]


a = Solution()

ans = a.modifiedGraphEdges(n, edges, source, destination, target)
