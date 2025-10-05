from typing import List
from collections import Counter

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        count = Counter(boxes)
        a = 0

        print(count)
        for i in boxes:
            a += count[i] * count[i]
            count[i] = 0
        return a



boxes = [1,3,2,2,2,3,4,3,1]
a = Solution()
ans = a.removeBoxes(boxes)
print(ans)