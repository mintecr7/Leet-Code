from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
      i = 0,
      n = len(nums)
      count = 1
      current = 0
      for i in range(n-1):
        j = i+1
        if nums[i] & nums[j] == 0:
            current = 2
            j += 1
            while j < n:
              print(f"current  {current}")
              print(f"current nums {nums[i]} and  {nums[j]}")
              if nums[i] & nums[j] == 0:
                 current +=1
                 j += 1
              else:
                i = j
                
                break
            count = max(count, current)
        else:
           continue
      return count




nums = [904163577,321202512,470948612,490925389,550193477,87742556,151890632,655280661,4,263168,32,573703555,886743681,937599702,120293650,725712231,257119393]

a = Solution()

ans  = a.longestNiceSubarray(nums=nums)

print(ans)