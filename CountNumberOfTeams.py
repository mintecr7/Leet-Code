from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0

        teams, n = 0, len(rating)
        for i, b in enumerate(rating):
            l = sum(a < b for a in rating[:i])
            r = sum(c > b for c in rating[i + 1 :])
            teams += l * r
            teams += (i - l) * (n - i - 1 - r)
        return teams


rating = [1, 2, 3, 4]

a = Solution()

ans = a.numTeams(rating)

print(ans)
