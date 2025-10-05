from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        jobs = sorted(zip(difficulty, profit))
        jobs.append((1000000, -100000))
        worker.sort()
        i = 0
        max_profit = 0
        total_profit = 0
        for ability in worker:
            while jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            total_profit += max_profit
        return total_profit



worker = [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]
profit = [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
difficulty = [66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]

a = Solution()

profit = a.maxProfitAssignment(difficulty, profit, worker)
print(profit)
