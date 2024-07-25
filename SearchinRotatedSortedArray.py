from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2

            if nums[0] <= nums[mid]:
                if nums[0] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid
        return left if nums[left] == target else -1

target = 3
nums = [3,5,1]

a = Solution()

ans = a.search(nums=nums, target=target)

print(ans)
