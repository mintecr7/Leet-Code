from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find_root(root_id):
            if parent[root_id] != root_id:
                parent[root_id] = find_root(parent[root_id])
            return parent[root_id]

        num_nodes = 10000
        parent = list(range(num_nodes * 2))
        for x, y in stones:
            parent[find_root(x)] = find_root(y + num_nodes)
        unique_roots = {find_root(x) for x, _ in stones}
        return len(stones) - len(unique_roots)


stones = [
    [3, 3],
    [4, 4],
    [1, 4],
    [1, 5],
    [2, 3],
    [4, 3],
    [2, 4],
]

a = Solution()

ans = a.removeStones(stones)

print(ans)
