from typing import List

class Solution:
		def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
			x_ranges = [[rec[0], rec[2]] for rec in rectangles]
			y_ranges = [[rec[1], rec[3]] for rec in rectangles]
			x_ranges.sort()
			y_ranges.sort()
			return self.checkValid(x_ranges) or self.checkValid(y_ranges)
		def checkValid(self, ranges: List[List[int]]) -> bool:
			r_start = ranges[0][0]
			r_end = ranges[0][1]
			cuts = 0
			for rng in ranges[1:]:
				if rng[0] == r_start:
					r_end = rng[1]
				elif rng[0] > r_start:
					if rng[1] <= r_end:
						continue
					else:
						if rng[0] >= r_end:
							cuts +=1 
						r_start = rng[0]
						r_end = rng[1]
				if cuts >=2 : 
					return True

			return cuts >= 2
n = 5
rectangles =[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

a = Solution()

ans = a.checkValidCuts(n=n, rectangles=rectangles)


print(ans)
 