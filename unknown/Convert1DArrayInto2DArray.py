from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        return [original[n * i : (i + 1) * n] for i in range(m)]


n = 1
m = 1
original = [1, 2]

a = Solution()

ans = a.construct2DArray(original, m, n)

print(ans)
