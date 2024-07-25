from typing import List
# from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        twoD_array = []
        # clone = Counter(nums)
        # print(clone)
        while nums:
            arr = []
            for i in nums:
                if nums[i] not in arr:
                    arr.append(nums[i])

        return twoD_array


nums = [1, 3, 4, 1, 2, 3, 1]

a = Solution()
ans = a.findMatrix(nums=nums)

print(ans)
