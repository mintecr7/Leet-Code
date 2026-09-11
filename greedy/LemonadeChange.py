from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            else:
                if tens:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0:
                return False
        return True


n = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]

a = Solution()


ans = a.lemonadeChange(n)

print(ans)
