from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (n + len(rolls)) * mean
        m = total - sum(rolls)

        if m < n or m > n * 6:
            return []

        missing = [m // n] * n

        for i in range(m % n):
            missing[i] += 1

        return missing


n = 10240
mean = 5
rolls = [
    4,
    1,
    4,
    3,
    3,
    5,
    3,
    5,
    4,
    2,
    3,
    1,
    2,
    6,
    2,
    4,
    2,
    5,
    5,
    5,
    2,
    2,
    4,
    6,
    6,
    5,
    3,
    1,
    5,
    1,
    1,
    1,
    3,
    1,
    2,
    1,
    3,
    2,
    2,
    5,
    2,
    1,
    6,
    5,
    2,
    2,
    5,
    2,
    5,
    3,
    1,
    2,
    6,
    3,
    6,
    1,
    1,
    6,
    1,
    3,
    5,
    5,
    3,
    5,
    5,
    3,
    1,
    6,
    5,
    1,
    6,
    4,
    1,
    3,
    3,
    6,
    3,
    3,
    3,
    6,
    1,
    3,
    2,
    4,
    4,
    5,
    6,
    6,
    3,
    4,
    3,
    2,
    5,
    6,
    2,
    6,
    5,
    1,
    4,
    4,
    5,
    2,
    2,
    6,
    4,
    2,
    3,
    5,
    3,
    3,
    4,
    6,
    3,
    6,
    2,
    3,
    1,
    2,
    2,
    5,
    2,
    3,
    5,
    5,
    3,
    4,
    1,
    4,
    4,
    3,
    4,
    5,
    4,
    3,
    4,
    1,
    3,
    2,
    5,
    1,
    5,
    4,
    3,
    6,
    5,
    2,
    1,
    1,
    2,
    2,
    6,
    5,
    6,
    4,
    1,
    6,
    5,
    5,
    6,
    3,
    5,
    3,
    2,
    6,
    2,
    3,
    5,
    6,
    6,
    3,
    4,
    5,
    6,
    6,
    3,
    1,
    5,
    4,
    6,
    6,
    3,
    3,
    2,
    5,
    6,
    3,
    2,
    1,
    3,
    1,
    6,
    6,
    5,
    4,
    2,
    5,
    5,
    1,
    4,
    5,
    3,
    5,
    1,
    3,
    4,
    3,
    5,
    3,
    5,
    3,
    6,
    3,
    6,
    4,
    2,
    3,
    2,
    4,
    1,
    1,
    1,
    6,
    1,
    3,
    5,
    3,
    4,
    4,
    3,
    6,
    1,
    6,
    2,
    1,
    4,
    1,
    2,
    6,
    4,
    3,
    4,
    2,
    5,
    2,
    6,
    1,
    4,
    1,
    1,
    5,
    5,
    4,
    2,
    3,
    4,
    5,
    1,
    5,
    1,
    4,
    6,
    6,
    3,
    6,
    6,
    1,
    6,
    2,
    5,
    3,
    6,
    2,
    5,
    3,
    3,
    3,
    6,
    4,
    5,
    3,
    3,
    3,
    6,
    3,
    2,
    6,
    3,
    2,
    3,
    3,
    5,
    5,
    5,
    3,
    6,
    5,
    1,
    6,
    4,
    5,
    1,
    4,
    1,
    5,
    1,
    3,
    3,
    1,
    5,
    5,
    6,
    4,
    6,
    2,
    5,
    2,
    1,
    3,
    5,
    6,
    5,
    4,
    5,
    2,
    1,
    6,
    6,
    6,
    5,
    5,
    5,
    6,
    1,
    4,
    6,
    4,
    4,
    5,
    5,
    3,
]

a = Solution()
ans = a.missingRolls(rolls, mean, n)

print(ans)
