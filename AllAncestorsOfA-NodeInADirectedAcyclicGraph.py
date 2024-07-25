from typing import List
from collections import defaultdict,deque

class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def breadth_first_search(start_node: int):
            queue = deque([start_node])
            visited = {start_node}
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        ans[neighbor].append(start_node)
        graph = defaultdict(list)
        ans = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])

        for edge in range(n):
            breadth_first_search(edge)
        return ans



n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

a = Solution()
ans =  a.getAncestors(n=n, edges=edgeList)

print (ans)
