class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        if len(heights) == 1:
            return [0,0]
        results = []
        rows, cols = len(heights), len(heights[0])
        
        def check_pacific(row: int, col: int)-> bool:
            top = True
            left = True
            r, c = row, col
            while r > 0:
                if heights[row][col] > heights[r][c]:
                    r -= 1
                else:
                    top = False
                    break
            while c > 0:
                if heights[row][col] > heights[row][c]:
                    c -=1
                else:
                    left = False
                    break
            return top and left
        
        
        def check_atlantic(row: int, col: int) -> bool:
            right = True
            bottom =  True 
            r, c = row, col
            while c in range(cols):
                if heights[row][col] > heights[r][c]:
                    c += 1 
                else:
                    right = False
                    break
            while r in range(rows):
                if heights[row][col] > heights[r][c]:
                    r += 1
                else:
                    bottom = False
                    break
            return right and bottom
        
        for r in range(rows):
            for c in range(cols):
                if check_pacific(r,c) and check_atlantic(r,c):
                    results.append([r,c])
        return results





heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]

ans =  Solution()
print(ans.pacificAtlantic(heights))
