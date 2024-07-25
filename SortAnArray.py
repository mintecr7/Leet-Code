from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        # insertion sort
        for i in range(1, len(nums)):
            pivot = nums[i]
            j = i - 1
            while j >= 0 and pivot < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = pivot
        """

        def merge(low: int, mid: int, high: int):
            tmp = []
            left = low
            right = mid + 1

            # compare and append
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    tmp.append(nums[left])
                    left += 1
                else:
                    tmp.append(nums[right])
                    right += 1

            # if elements on the left half are still not added
            while left <= mid:
                tmp.append(nums[left])
                left += 1

            # if elements on the right are still not added
            while right <= high:
                tmp.append(nums[right])
                right += 1
            for i in range(low, high + 1):
                nums[i] = tmp[i - low]

        # merge sort
        def merge_sort(low: int, high: int):
            if low >= high:
                return
            mid = (low + high) // 2
            merge_sort(low, mid)
            merge_sort(mid + 1, high)
            merge(low, mid, high)

        merge_sort(0, len(nums) - 1)

        return nums


nums = [5, 1, 1, 2, 0, 0]

a = Solution()

a.sortArray(nums)

print(nums)
