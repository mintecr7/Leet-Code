from typing import List


class Solution:
    def survivedRobotsHealths(
        self,
        positions: List[int],
        healths: List[int],
        directions: str,
    ) -> List[int]:
        r_healths = []
        n = len(positions)
        while True:
            i, j = 0, 1
            if j >= n:
                break
            for j in range(n):
                if directions[i] != directions[j]:
                    health_i, health_j = healths[i], healths[j]

                    if health_i > health_j:
                        print()

            break
        return r_healths


positions = [5, 4, 3, 2, 1]
healths = [2, 17, 9, 15, 10]
directions = "RRRRR"

a = Solution()
ans = a.survivedRobotsHealths(
    positions=positions, healths=healths, directions=directions
)
