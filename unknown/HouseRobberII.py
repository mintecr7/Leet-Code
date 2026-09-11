from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses: List[int]) -> int:
            rob1, rob2 = 0, 0
            for num in houses:
                new_rob = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        if len(nums) == 1:
            return nums[0]

        rob_excluding_last = rob_linear(nums[:-1])
        rob_excluding_first = rob_linear(nums[1:])
        return max(rob_excluding_last, rob_excluding_first)


nums = [2, 3, 2]

a = Solution()

ans = a.rob(nums)

print(ans)
