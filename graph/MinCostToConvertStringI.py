from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        look_up = {}
        tot = 0

        for i in range(len(cost)):
            key = original[i] + changed[i]
            look_up[key] = cost[i]

        print(look_up)

        for i in range(len(source)):
            key = source[i] + target[i]

            if key in look_up:
                print(key)
                tot += look_up[key]

        return tot


source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]


a = Solution()
ans = a.minimumCost(source, target, original, changed, cost)

print(ans)
