from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur_page = 0
        
        for log in logs:
            if log =="./":
                continue
            elif log == '../':
                if cur_page > 0:
                    cur_page -= 1
            else:
                cur_page += 1
        return cur_page


logs = ["d1/","../","../","../"]


a = Solution()

ans = a.minOperations(logs)

print(ans)