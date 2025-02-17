class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        comp = s[:2]
        fancy = comp

        for i in range(2, len(s) ):
            
            if comp[0] == s[i] and comp[-1] == s[i] :
                continue
            else:
                fancy += s[i]
                comp = comp[-1] + s[i]
        return fancy
      
s = "leeetcode"
a = Solution()

ans = a.makeFancyString(s)

print (ans) 