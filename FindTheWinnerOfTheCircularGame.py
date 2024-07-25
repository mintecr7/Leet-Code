
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        print(n, k)
        if n == 1:
            return 1
        else:
            return (self.findTheWinner(n-1, k)+k-1) % n + 1


n = 6
k = 5
a = Solution()
ans = a.findTheWinner(n, k)

print(ans)
