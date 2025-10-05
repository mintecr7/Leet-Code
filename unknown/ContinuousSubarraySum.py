from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        mp = {0: -1}

        for i in range(len(nums)):
            s += nums[i]
            r = s % k
            if r in mp and i - mp[r] >=2:
                return True
            if r not in mp:
                mp[r] = i
        return False


k = 6
nums = [23,2,6,4,7]

a = Solution()

ans = a.checkSubarraySum(nums=nums, k=k)

print(ans)
