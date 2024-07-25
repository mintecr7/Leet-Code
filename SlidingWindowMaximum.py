from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_vals = []
        curr_max = float('-inf')
        window = []
        for i in range (k):
            if nums[i] > curr_max:
                curr_max = nums[i]
            window.append(nums[i])

        max_vals.append(curr_max)

        for i in range (k, len(nums)):
            left = window.pop(0)
            window.append(nums[i])

            print(f"current poped {left}")
            print(f"cuurent max {curr_max}")
            print(f"new add value {nums[i]}")
            print(f"current max windo {window}")
            if nums[i] > curr_max:
                curr_max = nums[i]
            elif curr_max == left:
                curr_max = max(window)
            max_vals.append(curr_max)

        return max_vals

nums = [1,3,-1,-3,5,3,6,7]
a = Solution()

ans = a.maxSlidingWindow(nums=nums, k=3)

print(ans)
