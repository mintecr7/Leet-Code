from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])
        num_ppl = len(costs) // 2

        tot_cost = sum(costs[i][0] for i in range(num_ppl)) + sum(
            costs[i + num_ppl][1] for i in range(num_ppl)
        )
        return tot_cost


costs = [[10, 20], [30, 200], [400, 50], [30, 20]]

a = Solution()
ans = a.twoCitySchedCost(costs)

print(ans)
