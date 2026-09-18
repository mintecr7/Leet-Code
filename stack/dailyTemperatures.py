class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        # i, j = 0,1
        stack = []
        results = [0 for i in test]
        n = len(temperatures) 

        if n == 0:
            return [0]


        for i in range(0, n):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                waiting_indx = stack.pop()
                dif = i - waiting_indx
                results[waiting_indx] = dif
            stack.append(i)


        return results

  



test = [30,60,90]
a = Solution()

ans = a.dailyTemperatures(test)

print(ans)