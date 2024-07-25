class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        look_up = [str(i) for i in range(10)]
        s = s.strip()
        is_neg = False

        for i in range(len(s)):
            if i == 0:
                if s[i] == "-":
                    is_neg = True
                elif s[i] == "0" or s[i] == "+":
                    continue
                elif s[i] not in look_up:
                    return 0
                else:
                    res += s[i]
            else:
                if s[i] in look_up:
                    res += s[i]
                else:
                    break
        if res == "":
            return 0
        if is_neg:
            res = min(int(res), 2**31) * -1
        else:
            res = min(int(res), 2**31 - 1)

        return res


s = "0-1"

a = Solution()

ans = a.myAtoi(s)
print(ans)
