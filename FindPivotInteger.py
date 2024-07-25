class Solution:
    def pivotInteger(self, n: int) -> int:
        _sum = sum([i for i in range(1, n+1)])
        pivot = n
        _comp = 0

        while True:
            print(f"sum : {_sum}")
            print(f"pivot : {pivot}")
            print(f"right side: {_comp}")

            print(f"{_sum - pivot} vs {pivot + _comp}")

            if _sum  == pivot + _comp:
                return pivot
            elif _sum >= (pivot ) + _comp:
                _comp += pivot
                _sum -= pivot
                pivot -= 1

            else:
                break

        return -1

a = Solution()
print(a.pivotInteger(8))
