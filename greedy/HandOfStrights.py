from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for i in hand:
            if count[i]:
                for j in range(i, i+groupSize):
                    if count[j] == 0:
                        return False
                    count[j] -=1
                    if count[j] == 0:
                        count.pop(j)
        return True


hand = [1,1,2,2,3,3]
groupSize = 3
a = Solution()
ans = a.isNStraightHand(hand=hand, groupSize=groupSize)

print(ans)
