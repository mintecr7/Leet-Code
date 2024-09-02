"""
You have intercepted a secret message encoded as a string of numbers.
The message is decoded via the following mapping:
"1" -> 'A' ,"2" -> 'B' ... "25" -> 'Y' ,"26" -> 'Z'
However, while decoding the message, you realize that there are many
different ways you can decode the message because some codes are
contained in other codes ("2" and "5" vs "25").
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
            print(dp)
        return dp[0]


s = "11106"

a = Solution()
ans = a.numDecodings(s)

print(ans)
