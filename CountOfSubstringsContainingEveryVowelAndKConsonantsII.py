class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
      n =  len(word)
      window = 5 + k 
      count = 0
      if n < window:
         return count
      elif k == 0:
        if self.k_zero():
          return 1
        else:
          return 0
      elif n == window:
        if self.check_substring(word):
          return 1
        else:
          return 0
      print(f"passed, with range {n-window}")
      for i in range(n  - window): 
        if self.check_substring(word[i : i + window]):
          count += 1
         

      return count
    

    def check_substring(self, sub_str: str ) -> bool:

      vowls = 'aeiou'
      print(sub_str)
      for vowl in vowls:
        if sub_str.count(vowl) != 1:
          
          return False
      return True

    def k_zero(self) -> bool:
      vowls = 'aeiou'
      for vowl in  vowls:
        if vowl not in vowls:
          return False
      return True


k = 0
word = "aeueio"

a = Solution()

ans = a.countOfSubstrings(word=word, k=k)

print(ans)