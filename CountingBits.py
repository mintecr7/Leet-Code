from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            print(f"left shit {i >> 1} {i}")
            print(f"and operation {i & 1}")
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


n = 5

a = Solution()
ans = a.countBits(n)

print(ans)
