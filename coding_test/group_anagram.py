from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord("a")] += 1
        
            anagram[tuple(count)].append(i)
        
        return anagram.values()