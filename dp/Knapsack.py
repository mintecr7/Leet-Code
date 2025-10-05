from typing import List


class Solution:
    def knapsack(self, profit: List[int], weights: List[int], max_weight: int) -> int:
        n = len(profit)
        grid = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, max_weight + 1):
                if weights[i - 1] <= w:
                    grid[i][w] = max(
                        profit[i - 1] + grid[i - 1][w - weights[i - 1]], grid[i - 1][w]
                    )
                else:
                    grid[i][w] = grid[i - 1][w]

        # print(grid)

        print("DP Table:")
        for row in grid:
            print(row)

        return grid[n][max_weight]


profit = [3000, 2000, 1500, 2000]
weight = [4, 3, 1, 1]
W = 4


a = Solution()

ans = a.knapsack(profit, weight, W)

print(ans)
