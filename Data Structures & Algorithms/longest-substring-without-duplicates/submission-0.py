class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_chars = {}
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in used_chars and used_chars[char] >= start:
                start = used_chars[char] + 1

            used_chars[char] = i

            max_length = max(max_length, i - start + 1)
            
        return max_length