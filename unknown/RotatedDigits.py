from functools import lru_cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(position, is_good, is_limit):
            if position == 0:
                return 1 if is_good else 0

            upper_bound = digits[position] if is_limit else 9
            valid_numbers = 0
            for digit in range(upper_bound + 1):
                if digit in (0, 1, 8):
                    valid_numbers += dfs(
                        position - 1, is_good, is_limit and digit == upper_bound
                    )
                elif digit in (2, 5, 6, 9):
                    valid_numbers += dfs(
                        position - 1, 1, is_limit and digit == upper_bound
                    )

            return valid_numbers

        digits = [0] * 6
        length = 1
        while n:
            digits[length] = n % 10
            n //= 10
            length += 1

        return dfs(length, 0, True)


n = 10

a = Solution()
ans = a.rotatedDigits(n)

print(ans)
