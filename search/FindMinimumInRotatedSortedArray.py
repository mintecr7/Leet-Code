from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid =  (right + left)//2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]

nums = [2,3,4,5,1]
a = Solution()

ans = a.findMin(nums=nums)

print(ans)
