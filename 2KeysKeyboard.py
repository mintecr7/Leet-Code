"""
There is only one character 'A' on the screen of a notepad.
You can perform one of two operations on this notepad for each step:
    - Copy All: You can copy all the characters present on the screen
        (a partial copy is not allowed).
    - Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get
the character 'A' exactly n times on the screen.
"""


class Solution:
    def minSteps(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i: int):
            if i == 1:
                return 0
            count = i
            divisor = 2
            while divisor**2 <= i:
                if i % divisor == 0:
                    count = min(count, dfs(i // divisor) + divisor)
                divisor += 1
            return count

        return dfs(n)


n = 1

a = Solution()


ans = a.minSteps(n)

print(ans)
