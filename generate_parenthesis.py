class Solution:
    def generateParenthesis(self, n: int) -> list[str]:


        stack = []
        res = []

        def backtrack(openN: int, closedN: int) :
            if openN == closedN == n:

                return res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN +1, closedN)
                stack.pop()

            if closedN < n and closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0,0)

        return res

a = Solution()

ans =  a.generateParenthesis(3)

print(ans)
