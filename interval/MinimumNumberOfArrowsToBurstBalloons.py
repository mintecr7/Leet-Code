from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        _sorted = sorted(points, key=lambda x: x[1])

        overlapping = [[_sorted.pop(0)]]


        for i in _sorted:
            print(overlapping)
            if i[0] < overlapping[-1][-1][-1]:
                overlapping[-1].append(i)
            else:
                overlapping.append([i])

        return len(overlapping)

points =[[10,16],[2,8],[1,6],[7,12]]
a = Solution()

a.findMinArrowShots(points=points)
