from bisect import bisect_left


class Solution:
		def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
			def check(k: int) -> bool:
				dif = [0] * (len(nums) + 1)
				for left, right, value in queries[:k]:
						dif[left] += value
						dif[right + 1] -= value
		
				tot_sum = 0
				for original_value, change in zip(nums, dif):
						tot_sum += change
						if original_value > tot_sum:
								return False
				return True
			num_queries = len(queries)
			l = bisect_left(range(num_queries + 1), True, key=check)
			return -1 if l > num_queries else l



nums = [4,3,2,1]
queries = [[1,3,2],[0,2,1]]

a = Solution()

ans = a.minZeroArray(nums=nums, queries=queries)

print(ans)