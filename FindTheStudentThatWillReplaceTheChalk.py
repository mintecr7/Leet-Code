from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        tot = sum(chalk)
        if n == 1:
            return 0
        while k > tot:
            k -= tot

        for i in range(n):
            print(f"current index: {i} and current k: {k}")
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0


k = 22
chalk = [5, 1, 5]

a = Solution()

ans = a.chalkReplacer(chalk, k)

print(ans)
