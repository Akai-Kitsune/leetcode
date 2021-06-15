# 3. Longest Substring Without Repeating Characters
# result: Runtime: 40 ms, faster than 89.25% of Python
# Memory Usage: 14.3 MB, less than 35.19% of Python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :r,type: int
        """
        (i, result) = (0, 0)
        mp = {}
        for k in range(len(s)):
        	if s[k] in mp:
        		i = max(mp[s[k]], i)
        	else:
        		result = max(result, k-i+1)
        		mp[s[k]] = k + 1
        return result

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

# Input: s = ""
# Output: 0
