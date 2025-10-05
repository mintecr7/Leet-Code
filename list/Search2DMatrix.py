from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
            This function takes two arguments: 'matrix'(2D list of integers) and 'target' (integer).
            It performs two binary searches to find if the 'target' exists in the 'matrix'.

            The first binary search is performed along the depth (m) of the matrix to identify the row that could contain the target.
            The second binary search is performed along the identified row (n) to find 'target'.

            If the 'target' is found, the function returns 'True', otherwise 'False'.

            As the function performs two binary searches, the time complexity is O(log(m * n)).
        """

        def check(nums: List[int]):
            low, high = 0, len(nums) - 1
            while low <=  high:
                mid = low + ( high - low) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return False

        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = top + (bottom - top) //2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return check(matrix[mid])
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        return False
