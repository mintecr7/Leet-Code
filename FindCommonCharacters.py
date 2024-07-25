
from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans  = []
        res = words[0]
        # let =
        count = Counter(res)
        check =

        for i in range(1, len(words) ):
            # print(words[i], res)
            res = set(res).intersection(words[i])
            check = Counter(words[i])
            for letter in words[i]:
                if letter in count :
                    count[letter] = check[letter]

            # res = "".join(res)
        for i in res:
            for j in range(count[i]):
                ans.append(i)
        return ans

words = ["bella","label","roller"]
a = Solution()

ans  = a.commonChars(words=words)

print(ans)
