from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        look_pu = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 1:
            return look_pu[digits[0]]

        def combine_list(*lists):
            # print(*lists)

            combs = itertools.product(*lists)
            return ["".join(comb) for comb in combs]

        return combine_list(*(look_pu[i] for i in digits))


digits = "23"

a = Solution()
ans = a.letterCombinations(digits)

print(ans)
