class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l, r = 0, len(s1)
        sub_st = s2[:r]

        while r <= len(s2):
            print(f" current sub string {sub_st} at right {r} and left {l}")
            if sorted(sub_st) == sorted(s1):
                return True
            else:

                l+=1
                r+=1
            sub_st= s2[l:r]

        return False

s1 ="adc"
s2 = "dcda"

a = Solution()

ans =a.checkInclusion(s1, s2)

print(ans)
