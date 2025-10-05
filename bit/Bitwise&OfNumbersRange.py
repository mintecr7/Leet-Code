class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift


a  = Solution()
print(a.rangeBitwiseAnd(600000000,2147483645))
