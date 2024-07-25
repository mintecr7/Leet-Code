class Solution:
    def customSortString(self, order: str, s: str) -> str:
        r_s = ''
        for i in order:
            if i in s:
                r_s += i * s.count(i)
                s= s.replace(i,'')

        r_s += s
        return r_s


s = "xwvee"
order = "exv"


a = Solution()
a.customSortString(order=order, s=s)
