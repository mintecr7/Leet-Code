"""_summary_

Returns:
    _type_: _description_
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32-bit mask (avoid integer overflow)
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


x = 2
y = 3

a = Solution()

ans = a.getSum(x, y)

print(ans)
