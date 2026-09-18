"""_summary_

Returns:
    _type_: _description_
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = res | (((n >> i) & 1) << (31 - i))
        return res


n = 43261596

a = Solution()
ans = a.reverseBits(n)
print(ans)
