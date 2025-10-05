from typing import List

class Solution:
	def maximumTripletValue(self, nums: List[int]) -> int:
		
		res, i, d  = 0, 0, 0

		for num in nums:
			res = max(res, d * num)
			d = max(d, i-num)
			i = max(i, num)

		return res


nums = [12,6,1,2,7]

a = Solution()

ans = a.maximumTripletValue(nums=nums)

print(ans)

