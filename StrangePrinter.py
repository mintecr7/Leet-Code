"""
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and 
ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[101] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n ):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    for k in range(i,j):
                        dp[i][j] = min(
                            dp[i][j], 
                            dp[i][k] + dp[k+1][j]
                        )
        return dp[0][-1]
    

s = "abcabc"

a = Solution()
ans = a.strangePrinter(s)

print(ans)