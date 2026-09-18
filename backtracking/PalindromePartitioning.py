from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        parts = []
        pal = []

        def dfs(i):
            if i >= len(s):
                parts.append(pal[::])
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    pal.append(s[i : j + 1])
                    dfs(j + 1)
                    pal.pop()

        dfs(0)
        return parts

    def isPal(self, s: str, start: int, end: str) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            end -= 1
            start += 1

        return True


s = "aab"

a = Solution()

ans = a.partition(s)

print(ans)
