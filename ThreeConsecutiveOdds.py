from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n-2):
            if (arr[i] + arr[i + 1] + arr[i + 2]) % 2 != 0:
                return True

        return False
