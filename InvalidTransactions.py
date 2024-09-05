from typing import List
from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = defaultdict(list)
        idx = set()

        for i, x in enumerate(transactions):
            name, time, amount, city = x.split(",")
            time, amount = int(time), int(amount)
            d[name].append((time, city, i))

            if amount > 1000:
                idx.add(i)
            for t, c, j in d[name]:
                if c != city and abs(time - t) <= 60:
                    idx.add(i)
                    idx.add(j)
        return [transactions[i] for i in idx]


transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
a = Solution()
ans = a.invalidTransactions(transactions)
print(ans)
