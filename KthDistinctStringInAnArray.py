from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        for char in count:
            if count[char] == 1:
                k -= 1
            if k == 0:
                return char
        return ""

        # return dist[k - 1]


arr = ["aaa", "aa", "a"]
k = 1

a = Solution()

ans = a.kthDistinct(arr, k)

print(ans)
