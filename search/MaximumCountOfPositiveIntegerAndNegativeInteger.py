from typing import List

class Solution:
		def maximumCount(self, nums: List[int]) -> int:
			n = len(nums)
			i = n // 2 -1 
			j = n // 2
			if nums[0] == 0 and nums[-1] == 0:
				return 0
			if nums[0] <= -1 and nums[-1] <= -1 or nums[0] >= 1 and nums[-1] >=1:
				return n
		
			while i > 0 and j < n:
				if nums[i] <= -1 and nums[j] >= 1:
					break
				if nums[i] > -1 :
					i = i // 2
				if nums[j] < 1:
					j += (n-j)//2 + 1

			
			while i < j:
				if nums[i + 1] >= 0 and nums[j - 1] <= 0:
					break
				if nums[i + 1] < 0:
					i +=1 
				if nums[j - 1] > 0:
					j -= 1
			return max(i+1, n-j)



nums =[-2,-1,-1,1,2,3]
a = Solution()

ans = a.maximumCount(nums=nums)

print(ans)