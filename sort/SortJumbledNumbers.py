from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []

        for num in nums:
            curr = str(num)
            order = ""
            for i in curr:
                order += str(mapping[int(i)])
            mapped.append(int(order))

        pairs = list(zip(nums, mapped))
        pairs.sort(key=lambda x: x[1])
        nums = [x[0] for x in pairs]
        return nums


mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [789, 456, 123]

a = Solution()

ans = a.sortJumbled(mapping, nums)

print(ans)
