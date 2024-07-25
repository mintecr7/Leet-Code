from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j =  0, 0
        _intersection = []
        n_1, n_2 = len(nums1), len(nums2)

        while i < n_1:
            if nums1[i] in nums2 and nums1[i] not in _intersection:
                _intersection.append(nums1[i])
                i +=1
            else:
                i += 1
        while j < n_2:
            if nums2[j] in nums1 and nums2[j] not in _intersection:
                _intersection.append(nums2[j])
                j +=1
            else:
                j += 1


        return _intersection


a  = Solution()
print(a.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
