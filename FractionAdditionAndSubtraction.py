"""
Given a string expression representing an expression of fraction addition and subtraction, 
return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, 
change it to the format of a fraction that has a denominator 1. 
So in this case, 2 should be converted to 2/1.

"""
from fractions import Fraction

class Solution:
    def float_to_fraction_str(self, number):

        fraction = Fraction(number).limit_denominator()
        
        numerator = fraction.numerator
        denominator = fraction.denominator
        if numerator < 0 < denominator:
            fraction_str = f"-{abs(numerator)}/{denominator}"
        else:
            fraction_str = f"{numerator}/{denominator}"

        return fraction_str
    def fractionAddition(self, expression: str) -> str:
        n = len(expression)
        sing = 1
        ops = ["+", "-"]
        sum = 0
        i = 0
        while i < n:
            if expression[i] == "-":
                sing = -1
            elif expression[i] == "+":
                sing = 1
            else:
                frac = ""
                while i < n and expression[i] not in ops:
                    frac += expression[i]
                    i += 1
                i -= 1
                frac = frac.split("/")
                sum += int(frac[0])/int(frac[-1]) * sing
            i += 1
        return self.float_to_fraction_str(sum)




expression = "-1/2+1/2+1/3"

a = Solution()
ans = a.fractionAddition(expression)

print(ans)