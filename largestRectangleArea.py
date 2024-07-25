class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            if len(stack) == 0:
                stack.append([i, heights[i]])
            else:
                if stack[-1][1] <= heights[i]:
                    stack.append([i, heights[i]])
                else:
                    last_index = stack[-1][0]
                    while len(stack) > 0 and stack[-1][1] > heights[i]:
                        top = stack.pop()
                        area = (i-top[0]) * top[-1]
                        last_index = top[0]
                        max_area = max(max_area, area)
                    stack.append([last_index, heights[i]])

        return  max_area


        



# heights = [2,1,5,6,2,3]
# heights = [2,1,2]
heights = [2,4]

ans = Solution()
print(ans.largestRectangleArea(heights))