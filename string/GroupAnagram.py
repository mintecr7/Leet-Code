from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for word in strs:
            if "".join(sorted(word)) in anagrams.keys():
                anagrams["".join(sorted(word))].append(word)
            else:
                anagrams["".join(sorted(word))] =  [word]

        return anagrams.values()
