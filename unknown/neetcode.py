

# def groupAnagrams(strs):
#     anagram_groups = {}
    
#     for word in strs:
#         sorted_word = "".join(sorted(word))
#         if sorted_word in anagram_groups:
#             anagram_groups[sorted_word].append(word)
#         else:
#             anagram_groups[sorted_word] = [word]
#     print(anagram_groups)
#     grouped_anagrams = list(anagram_groups.values())
#     return grouped_anagrams

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = groupAnagrams(strs)
# print(result)

# def topKFrequent( nums, k):
    #"""
   # :type nums: List[int]
    #:type k: int
    #:rtype: List[int]
    #"""
    # num_count = {}

    # for num in nums:
    # 	print(num_count)
    # 	if num in num_count:
    # 		num_count[num] +=1
    # 	else:
    # 		num_count[num] = 0

    # sorted_keys =  sorted(num_count, key=lambda key: num_count[key], reverse=True)
    # top_keys = sorted_keys[:k]
    # return top_keys


# nums = [1,1,1,2,2,3]
# topKFrequent(nums, 2)

# def productExceptSelf(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     n = len(nums)
#     left_products = [1] * n
#     right_products = [1] * n
#     result = [1] * n
    
#     left_product = 1
#     for i in range(n):
#         left_products[i] = left_product
#         print(left_product)
#         left_product *= nums[i]
#     print(left_products)
#     right_product = 1
#     for i in range(n - 1, -1, -1):
#         right_products[i] = right_product
#         right_product *= nums[i]
    
#     for i in range(n):
#         result[i] = left_products[i] * right_products[i]

#     return result



# nums = [1,2,3,4]
# productExceptSelf(nums)





# def plusOne(digits: list[int]) -> list[int]:


# 	num_str = "".join(str(i) for i in digits)
# 	num =int(num_str) + 1
# 	answer = [int(i) for i in str(num)]


# 	print(answer)





# digits = [4,3,2,1]
# plusOne(digits)

# def isValidSudoku(board: list[list[str]]) -> bool:
# 	row = {}
# 	col = {}
# 	box = {(0,0):[], (0,1): [], (0,2):[],
# 		   (1,0):[], (1,1): [], (1,2):[],
# 		   (2,0):[], (2,1): [], (2,2):[]
# 	}

# 	for i in range(9):
# 		col.setdefault(i, [])
# 		row.setdefault(i, [])

	
# 	for i in range(9):
# 		for j in range(9):
# 			if board[i][j] == ".":
# 				continue
# 			if (board[i][j] in row[i] 
# 				or board[i][j] in col[j] 
# 				or board[i][j] in box[(i//3, j//3)]):
# 				print(board[i][j], (i,j))
# 				print(row, col)

# 				return False
# 			row[i].append(board[i][j])
# 			col[j].append(board[i][j])
# 			box[(i//3,j//3)].append(board[i][j])


# 	return True




# board =	[
# 		["8","3",".",".","7",".",".",".","."],
# 		["6",".",".","1","9","5",".",".","."],
# 		[".","9","8",".",".",".",".","6","."],
# 		["8",".",".",".","6",".",".",".","3"],
# 		["4",".",".","8",".","3",".",".","1"],
# 		["7",".",".",".","2",".",".",".","6"],
# 		[".","6",".",".",".",".","2","8","."],
# 		[".",".",".","4","1","9",".",".","5"],
# 		[".",".",".",".","8",".",".","7","9"]
# 		]


# print(isValidSudoku(board))



# def longestConsecutive(nums: list[int])-> int:
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     nums = sorted(nums)
#     temp = [nums[0]]
#     longest = [nums[0]]
#     for i in range(1, len(nums)):
#     	if nums[i] == temp[-1]+1:
#     		temp.append(nums[i])
#     	else:
#     		if len(temp)>len(longest):
#     			longest = temp
#     			temp = [nums[i]]
#     		else:
#     			temp= [nums[i]]
#     if len(temp)>len(longest):
#     	longest = temp
#     	temp = [nums[i]]

#     return len(longest) 



# nums = [1,2,0,1]

# nums_2 = [0,3,7,2,5,8,4,6,0,1]

# print(longestConsecutive(nums))


# def majorityElement( nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     num_count = {}

#     for num in nums:
#     	print(num_count)
#     	if num in num_count:
# #     		num_count[num] +=1
# #     	else:
# #     		num_count[num] = 0

# #     return max(num_count, key=num_count.get)




# # nums = [3,2,3]
# # majorityElement(nums)
# # import re
# # def isPalindrome(s: str)-> bool:
# #     """
# #     :type s: str
# #     :rtype: bool
# #     """
# #     s = re.sub(r'[^a-zA-Z0-9]', '', s)
# #     n = len(s)
# #     strs = list(s.lower())
# #     if n% 2 == 0:
# #     	a = strs[0:n/2]
# #     	b = strs[n/2:]
# #     	print (a ==b[::-1])
# #     else: 
# #     	a = strs[0:n//2]
# #     	b = strs[n//2+1:]
# #     	print (a ==b[::-1])


# # s = "A man, a plan, a canal: Panama"




# # isPalindrome(s)




# def twoSum( numbers: list[int], target: int) :
#     """ 
#     :type numbers: List[int]
#     :type target: int
#     :rtype: List[int]
#     """

#     # start = 0
#     num_to_index = {}
#     sums = []

    
#     for i, num in enumerate(numbers):
#         complement = target - num
#         if complement in num_to_index:
#         	a = sorted([num_to_index[complement] , num, -target])
#         	if a not in sums:
#         		sums.append(a)
#             # return (num_to_index[complement] , num)
#         num_to_index[num] = num

#     # print(sums)
#     return sums







# def threeSum( nums):
# 	"""
# 	:type nums: List[int]
# 	:rtype: List[List[int]]
# 	"""
# 	nums.sort()
# 	result = []
# 	for i in range(len(nums) - 2):
# 		if i > 0 and nums[i] == nums[i - 1]:
# 			continue
# 		l, r = i + 1, len(nums) - 1
# 		while l < r:
# 			s = nums[i] + nums[l] + nums[r]
# 			if s < 0:
# 				l += 1
# 			elif s > 0:
# 				r -= 1
# 			else:
# 				result.append([nums[i], nums[l], nums[r]])
# 				while l < r and nums[l] == nums[l + 1]:
# 					print((l,r) , "duplicate of first pointer skipped", nums, i)
# 					l += 1
# 				while l < r and nums[r] == nums[r - 1]:
# 					print(l , "duplicate of second pointer skipped", nums, i)
# 					r -= 1
# 				l += 1
# 				r -= 1
# 	return result

# nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# print(threeSum(nums))


# def maxArea(height: list[int]) ->  int:
# 	"""
# 	:type height: List[int]
# 	:rtype: int
# 	"""
# 	result = 0
# 	i, j =  0, len(height)-1

# 	while i < j:
# 		temp = 0
# 		if height[i] > height[j]:
# 			temp = abs(i-j) * height[j]
# 			j -= 1
# 		else:
# 			temp = abs(i-j) * height[i]
# 			i -=1
# 		if temp > result:
# 			result = temp

# 	return  result




# height = [10,9,8,7,6,5,4,3,2,1]


# print(maxArea(height))



# def trap(height):
#     """
#     :type height: List[int]
#     :rtype: int
#     """
#     count = 0
#     i, j =  0, len(height)-1
#     left_tall, right_tall = 0,0

#     while i < j:
#     	if height[i] >= left_tall:
#     		left_tall = height[i]

#     	else:
#     		count += left_tall - height[i]
   


#     	if height[j] >= right_tall:
#     		right_tall = height[j]
#     	else:
#     		count += right_tall - height[j]

#     	if height[i] > height[j]:
#     		j -= 1
#     	else:
#    			i += 1


#     return count






# # height = [0,1,0,2,1,0,1,3,2,1,2,1]	
# height = [4,2,0,3,2,5]

# print(trap(height))




# def isValid(s: str) -> bool:
#     """
#     :type s: str
#     :rtype: bool
#     """
#     map_dic = {'}': '{', ")": "(", ']':'['}
#     stack = []

#     for i in s:
#     	if i not in map_dic.keys():
#     		stack.append(i)
#     	else:
#     		if len(stack) > 0 and stack[-1] == map_dic[i]:
#     			stack.pop(-1)
#     		else:
#     			return False

#     print(stack)

#     return len(stuck) == 0

# s = "()"   
# # s = "()[]{}"

# print(isValid(s))


# class MinStack(object):

#     def __init__(self):
#         self.stack = []
#         self.length = 0
#         self.min = 2**31 - 1
#         self.currMin = [self.min]
#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.stack.append(val)
#         self.length += 1
#         i = 0

#         while i < self.length:

#         	if self.currMin[i] > val:
        		
#         		self.currMin.insert(i, val) 
#         		self.min = self.currMin[0]
#         		print(self.currMin, self.min)

#         		break
#         	else:
#         		i +=1
#         # print(self.stack, self.min, self.currMin)         
#     def pop(self):
#         """
#         :rtype: None
#         """
#         i = 0

#         if self.length > 0:
#             min_num = self.stack.pop(-1)
#             self.length -= 1
#             print(min_num, self.currMin)
#             if min_num == self.min:
#                 self.currMin.pop(0)
#                 self.min = self.currMin[0]
#             else:
#             	while i < self.length:
#             		if self.currMin[i] == min_num:
#             			print(self.currMin, i)
#             			self.currMin.pop(i+1)
#         # print(self.stack, self.min, self.currMin)


#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min
  

# obj = MinStack()

# obj.push(-2)
# obj.push(0)
# obj.push(-1)
# obj.getMin()
# obj.top()
# obj.pop()
# obj.getMin()
