# NOTE: 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?


# NOTE:
# SOLUTION: PYTHON3
from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        target_count = Counter(t)
        window_count = Counter()
        required = len(target_count)
        formed = 0
        left = right = 0
        min_length = float('inf')
        min_window = ""

        while right < len(s):
            char = s[right]
            window_count[char] += 1

            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]

                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1

                left += 1

            right += 1

        return min_window
        

# TIME COMPLEXITY:
