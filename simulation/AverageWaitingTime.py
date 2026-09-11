from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = customers[0][0]
        time = 0
        
        for customer in customers:
            if customer[0] > wait:
                wait = customer[0]
            
            wait += customer[-1]
            time += wait - customer[0]
    
        return time/ len(customers)
    
    

customers = [[5,2],[5,4],[10,3],[20,1]]

a = Solution()
ans = a.averageWaitingTime(customers)

print(ans)