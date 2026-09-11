"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            left, right = i, i
            while left in range(n) and right in range(n):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
                count += 1
            left, right = i, i + 1
            while left in range(n) and right in range(n):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
                count += 1

        return count


s = "abc"

a = Solution()
ans = a.countSubstrings(s)

print(ans)
