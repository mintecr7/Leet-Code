from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        conc = dict()
        importance = dict()
        max_impt = 0

        for i, j in roads:
            if i in conc:
                conc[i] += 1
            else:
                conc[i] = 1
            if j in conc:
                conc[j] += 1
            else:
                conc[j] = 1

        keys = sorted(conc, key=conc.get, reverse=True)

        for key in keys:
            importance[key] = n
            n -= 1
        for i, j in roads:
            max_impt += (importance[i] + importance[j])
        return  max_impt



n = 5
roads = [[0,3],[2,4],[1,3]]
a = Solution()
ans = a.maximumImportance(n=n, roads=roads)

print(ans)
