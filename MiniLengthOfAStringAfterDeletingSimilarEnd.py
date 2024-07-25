class Solution:
    def minimumLength(self, s: str) -> int:

        while True:
            if len(s) == 0 or len(s) ==1:
                break
            if s[0] ==s[-1]:
                char = s[0]
                while s[0] == char:
                    s = s[1:]
                    if len(s) == 0:
                        break
                while len(s) !=0 and s[-1] == char:
                    s = s[: -1]
                    if len(s) == 0:
                        break

            else:
                break
        return len(s)

a = Solution()
s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"

ans = a.minimumLength(s)
print(ans)
