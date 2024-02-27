# NOTE: 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 
# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

# NOTE:

# SOLUTION: PYTHON3
from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1
        
# TIME COMPLEXITY:
