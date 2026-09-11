"""
For example, if s = "zbax" and k = 2,
then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # convert = ""
        convert = "".join([str(ord(s[i]) - 96) for i in range(len(s))])

        for i in range(k):
            transform = 0

            for char in convert:
                transform += int(char)
            convert = str(transform)
        return int(convert)


k = 2
s = "leetcode"

a = Solution()
ans = a.getLucky(s, k)

print(ans)
