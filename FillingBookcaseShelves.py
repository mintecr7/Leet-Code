from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        min_height = [0] * (n + 1)
        for i, (width, height) in enumerate(books, 1):
            min_height[i] = min_height[i - 1] + height
            total_width = width

            for j in range(i - 1, 0, -1):
                total_width += books[j - 1][0]

                if total_width > shelfWidth:
                    break

                height = max(height, books[j - 1][1])
                min_height[i] = min(min_height[i], min_height[j - 1] + height)
            print(min_height)
        return min_height[n]


books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelfWidth = 4

a = Solution()

ans = a.minHeightShelves(books, shelfWidth)

print(ans)
