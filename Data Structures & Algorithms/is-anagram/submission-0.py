from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        if Counter(list_s) == Counter(list_t):
            return True
        return False