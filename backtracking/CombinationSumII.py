from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sums = []

        # candidates.sort()

        def dfs(start: int, cur: List[int], total: int):
            if total == target:
                sums.append(cur[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()

        dfs(0, [], 0)
        return sums


target = 8
candidates = [10, 1, 2, 7, 6, 1, 5]


a = Solution()
ans = a.combinationSum(candidates=candidates, target=target)

print(ans)
