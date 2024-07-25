from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


a = Solution()
word = "ABCCED"

ans = a.exist(board=board, word=word)

print(ans)
