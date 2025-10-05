"""
leet code daily challenge 20242.08.06
You are given a string word containing lowercase English letters.
Telephone keypads have keys mapped with distinct collections of lowercase English letters,
which can be used to form words by pushing them. For example,
the key 2 is mapped with ["a","b","c"],
we need to push the key one time to type "a", two times to type "b",
and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
The keys can be remapped to any amount of letters,
but each letter must be mapped to exactly one key.
You need to find the minimum number of times the keys will be
pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below.
Note that 1, *, #, and 0 do not map to any letters.
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        cnt = [0 for _ in range(26)]
        for c in word:
            cnt[ord(c) - 97] += 1
        cnt.sort()
        print(cnt)
        for i in range(25, -1, -1):
            if cnt[i] == 0:
                break
            res += cnt[i] * ((25 - i) // 8 + 1)
        return res


word = "MinimumNumberOfPushesToTypeWordpy"
a = Solution()
ans = a.minimumPushes(word)

print(ans)
