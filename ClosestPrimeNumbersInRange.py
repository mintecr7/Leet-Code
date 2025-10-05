from typing import List
import math

class Solution:
	def closestPrimes(self, left: int, right: int) -> List[int]: 
		n = math.ceil((right ** (0.5)))
		iter_list = [True for _ in range(right+1)]
		primes = []
		for i in range(2, n + 1):
			if iter_list[i]:
				j = i**2
			while j < right :
				iter_list[j] = False
				j  +=  i
		for i in range(2, right+1):
			if iter_list[i] and i >= left:
				primes.append(i)
		if len (primes) < 2:
			return [-1, -1]

		small_window =  primes[1] - primes[0]
		window = [primes[0], primes[1]]
		iter_len = len(primes)
		print (primes)
		for i in range(1, iter_len):
			print(f"current small window: {small_window}, primes at i are {primes[i - 1]} and {primes[i]}")
			if primes[i] - primes[i-1] < small_window:
				window = [primes[i-1], primes[i]]
				small_window = primes[i] - primes[i-1]
		return window



left = 23
right = 25
a = Solution()
ans = a.closestPrimes(left=left, right=right)

print(ans)