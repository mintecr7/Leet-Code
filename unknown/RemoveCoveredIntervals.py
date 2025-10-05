from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) == 1:
            return 1

        remaining = len(intervals)
        # intervals = sorted(intervals)

        cur_int = intervals[0]

        for i in range(1,len(intervals)):

            if cur_int[0] <= intervals[i][0] and cur_int[1] >= intervals[i][1]:
                remaining -= 1
            elif cur_int[0] >= intervals[i][0] and cur_int[1] <= intervals[i][1]:
                remaining -= 1
                cur_int = intervals[i]
            else:
                cur_int = intervals[i]


        return remaining

intervals = [[1,4],[3,6],[2,8]]
a = Solution()

ans = a.removeCoveredIntervals(intervals=intervals)
print(ans)
