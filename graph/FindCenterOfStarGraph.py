from typing import List

class Solution:
    """
    To solve this problem, we can start by noticing that in a star graph,
    the center node will be the one shared by all the edges.
    Since we know that this graph is a star graph, we can conclude that
    the center must be one of the nodes from the first edge described in the edges array.
    We can conclude this about all of the edges.

    using this logic, by just looking for a repeated node in the first 2 edges we can find the center.
    """
    def findCenter(self, edges: List[List[int]]) -> int:

        edge = edges[0]

        if edges[1][0] in edge:
            return edges[1][0]
        else:
            return edges[1][1]




a = Solution()
edges = [[1,2],[5,1],[1,3],[1,4]]

ans = a.findCenter(edges=edges)

print(ans)
