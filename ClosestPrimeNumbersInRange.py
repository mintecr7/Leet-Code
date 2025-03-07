from typing import List
import math

class Solution:
	def closestPrimes(self, left: int, right: int) -> List[int]:
		n = math.ceil((right ** (0.5)))
		iter_list = [True for _ in range(right+1)]
		# nums = [i for i in range(right)]
		primes = []
		# print(len(iter_list))
		for i in range(2, n):
			if iter_list[i]:
				j = i**2
			while j < right + 1:
				# print(f"currernt j: {j} at curretn i: {i} ") 
				iter_list[j] = False
				j  +=  i

				# print(f"updated j: {j} at updated i: {i} ")
		for i in range(2, right):
			if iter_list[i] and i >= left:
				primes.append(i)
		if len (primes) < 2:
			return [-1, -1]
		# elif len(primes) == 2 and primes[0] == left and primes[right] == right:
		# 	return [-1,-1]
		else:
			small_window =  primes[1] - primes[0]
			window = [primes[0], primes[1]]
			iter_len = len(primes)

			for i in range(1, iter_len):

				if primes[i] - primes[i-1] < small_window:
					window = [primes[i-1], primes[i]]
					small_window = primes[i] - primes[i-1]
			return window


left = 23
right = 25
a = Solution()
ans = a.closestPrimes(left=left, right=right)

print(ans)