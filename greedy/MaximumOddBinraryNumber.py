class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_len = len(s)
        count =  s.count('1')
        max_binary = '0' * len(s)
        if count ==1:
            max_binary = '0' * (s_len -1 ) + '1'
        else:
            max_binary = ('1' * (count-1)) + ('0' * (s_len - count - 1)) + '1'
        return max_binary
