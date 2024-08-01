"""
_summary_
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1

        return count


n = 128

a = Solution()
ans = a.hammingWeight(n)

print(ans)
