class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = [(i+1) for i in range(n+1)]
        for i in range(n):
            if pattern[i] == 'I':
                if ans[i] >= ans[i + 1]:
                    new_val = ans[i]
                    while new_val < 9 and new_val in ans:
                        new_val += 1
                    ans[i + 1] = new_val
            else:
                if ans[i] <= ans[i + 1]:
                    new_val = ans[i + 1] 
                    while new_val in ans:
                        new_val -= 1
                    ans[i ] = new_val

        return "".join(str(i) for i in ans)

pattern = "IIIDIDDD"

a = Solution()
ans = a.smallestNumber(pattern)

print(ans)
print(ans)