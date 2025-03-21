from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] > self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        return True

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        min_weights = [-1] * n
        uf = UnionFind(n)
    
        for u, v, _ in edges:
            uf.union(u, v)
    
        for u, _, w in edges:
            root = uf.find(u)
            min_weights[root] &= w

        def query_cost(u: int, v: int) -> int:
            if u == v:
                return 0
            root_u, root_v = uf.find(u), uf.find(v)
            return min_weights[root_u] if root_u == root_v else -1
        return [query_cost(s, t) for s, t in queries]

      
n = 5 
query = [[0,3],[3,4]]
edges = [[0,1,7],[1,3,7],[1,2,1]]