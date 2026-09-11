import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = {i: [] for i in range(n)}
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        max_probs = [0] * n
        max_probs[start_node] = 1
        pq = [(-1, start_node)]

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob

            if node == end_node:
                return prob

            if prob < max_probs[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_probs[neighbor]:
                    max_probs[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return 0.0


n = 3
end = 2
start = 0
succProb = [0.5]
edges = [[0, 1]]

a = Solution()
ans = a.maxProbability(n, edges, succProb, start, end)

print(ans)
