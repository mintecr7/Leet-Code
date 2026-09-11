class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if s.isspace() or not str(s) or len(s)==1:
            return 1
        temp1 = []
        temp2 = []
        for i in range(len(s)):
            while i<len(s) and s[i] not in temp1:
                temp1.append(s[i])
                i+=1 
            if len(temp1) > len(temp2):
                temp2 = temp1
                temp1 = []
            temp1 = []
        return len(temp2)

