class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != "(" and s[j] != ")":
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1

            elif s[i] == "(" and s[j] != ")":
                j -= 1
            elif s[i] != "(" and s[j] == ")":
                i += 1
            else:
                i += 1
                j -= 1
        s = "".join(s)
        s = s.replace("(", "")
        s = s.replace(")", "")

        return s


s = "(u(love)i)"

a = Solution()
ans = a.reverseParentheses(s=s)

print(ans)
