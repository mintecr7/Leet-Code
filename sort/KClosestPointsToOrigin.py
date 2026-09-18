# import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        heap solution
        distances = []
            res = []
            for x, y in points:
                distance = (x**2 + y**2) ** 0.5
                distances.append([distance, x, y])
            heapq.heapify(distances)
            for _ in range(k):
                _, x, y = heapq.heappop(distances)
                res.append([x, y])
            return res
        """

        # sort solution
        def euclidean_distance(point):
            return point[0] ** 2 + point[1] ** 2

        points.sort(key=euclidean_distance)

        return points[:k]


points = [[0, 1], [1, 0]]
k = 2

a = Solution()

ans = a.kClosest(points, k)

print(ans)
