class Solution:
    def numSquares(self, n: int) -> int:
        per_squares =[]
        for i in range(1,n):
            sqr = i**2
            if sqr < n:
                per_squares.append(sqr)
            else:
                break
        print (per_squares)
        return n

a = Solution()
a.numSquares(13)
