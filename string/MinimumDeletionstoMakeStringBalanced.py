class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count("a")
        b_count, b_seen = s.count("b"), 0
        deletion = min(a_count, b_count)
        if deletion == 0:
            return deletion
        for char in s:
            if char == "a":
                a_count -= 1
            else:
                b_seen += 1
            deletion = min(deletion, a_count + b_seen)
        return deletion


s = "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"
a = Solution()

ans = a.minimumDeletions(s)

print(ans)
