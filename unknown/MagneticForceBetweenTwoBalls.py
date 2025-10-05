from typing import List

class Solution:
    def check(self, mid: int, m: int, pos : List[int]):
        prev_pos = pos[0]
        count = 1

        for i in pos[1:]:
            if i - prev_pos >= mid:
                prev_pos = i
                count +=1

        return count >= m

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        low, high = 1, position[-1] - position[0]

        while low < high:
            print(f"low is {low} and high is {high}")
            mid = (low + high + 1) // 2


            if self.check(mid, m, position):
                # print(mid)
                low = mid
            else:
                print()
                high = mid - 1

        return low

position = [1,2,3,4,7]
m = 3


a = Solution()

ans = a.maxDistance(position=position, m=m)

print(ans)
