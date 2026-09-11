class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        xa = "ab"
        ya = "ba"

        if s == "".join(sorted(s)):
            a_count = s.count("a")
            b_count = s.count("b")

            return min(a_count * x, b_count * x)

        if x < y:
            xa, ya = ya, xa
            x, y = y, x

        while "ab" in s or "ba" in s:
            if xa in s:
                count = s.count(xa)
                points += count * x
                s = s.replace(xa, "")

            elif ya in s:
                count = s.count(ya)
                points += count * y
                s = s.replace(ya, "")
        return points


s = "aabbaaxybbaabb"
x = 5
y = 4

a = Solution()
ans = a.maximumGain(s, x, y)

print(ans)
