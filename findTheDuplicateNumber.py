from typing import List
def findDuplicate(nums: List[int]) -> int:

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    p1 = nums[0]
    p2 = slow

    print (slow, fast)

    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]
        print(p1, p2)

    return p1
nums = [1,3,4,2,2]
findDuplicate(nums=nums)
