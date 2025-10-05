from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        content = 0
        s.sort()
        g.sort()
        i, j = 0, 0
        
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                content += 1
                i += 1
                j += 1
            elif s[i] < g[j]:
                i += 1
                
        
        
        return content 


g = [10,9,8,7]
s = [5,6,7,8]
a = Solution()

ans = a.findContentChildren(g, s)

print(ans)