from typing import List

class Solution:
	def maximumTripletValue(self, nums: List[int]) -> int:
		n = len(nums)
		max_multi = 0
		for i in range(n):
			for k in range(i+2, n):
				for j in range(i, k):
					multi = (nums[i] - nums[j]) * nums[k]
					if multi > max_multi:
						max_multi = multi

		return max_multi


nums = [12,6,1,2,7]

a = Solution()

ans = a.maximumTripletValue(nums=nums)

print(ans)

