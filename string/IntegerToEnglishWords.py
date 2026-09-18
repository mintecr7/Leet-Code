"""
273. Integer to English Words
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


class Solution:
    def __init__(self):
        self.tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        self.less_than_20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        self.thousands = ["Billion", "Million", "Thousand", ""]

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(num % 100)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        result = []
        i, j = 1000000000, 0

        while i > 0:
            if num // i != 0:
                result.append(self.helper(num // i))
                result.append(self.thousands[j])
                result.append(" ")
                num %= i
            j += 1
            i //= 1000

        return "".join(result).strip()


num = 1234567

a = Solution()

ans = a.numberToWords(num)

print(ans)
