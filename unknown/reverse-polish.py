
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ["*", "-", "/", "+"]

        for i in tokens:
            if i not in operators:
                stack.append(i)
                # print(stack)

            else:
                a = stack.pop()
                b = stack.pop()
                c = self.calculate(int(b), int(a), i)
                stack.append(c)
                # print(stack)

        return stack[0]


    def calculate(self, a: int, b: int, oper: str) -> float:

        # print(a,b)
        if oper == "*":
            return a * b
        elif oper == "/":
            return a / b
        elif oper == "+":
            return a + b
        else:
            return a - b

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

solution = Solution()
ans = solution.evalRPN(tokens)

print(ans)
