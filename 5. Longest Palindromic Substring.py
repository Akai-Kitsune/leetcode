# 5. Longest Palindromic Substring
# Runtime: 124 ms, faster than 97.72% of Python3 
# online submissions for Longest Palindromic Substring.
# Memory Usage: 14.6 MB, less than 24.68% of Python3 
# online submissions for Longest Palindromic Substring.

class Solution(object):
    # Using Manacher's algorithm
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        pld1 = [0] * size
        pld2 = [0] * size
        (i, j) = (0, -1)
        mx1, index1= 0, 0
        n = 0
        #We find odd subpalindriomes end make array pld1.
        while n < size:
            k = (1 if n > j else min(pld1[i+j-n], j - n + 1))
            #Search for subpalindromes
            while (n+k<size) and (n-k>=0) and (s[n+k] == s[n-k]):
                k += 1
            pld1[n] = k - 1
            if n + k - 1 > j:
                i = n - k + 1
                j = n + k - 1
            if pld1[n] > mx1:
                mx1 = pld1[n]
                index1 = n
            n += 1
        (i, j) = (0, -1)
        mx2, index2= 0, 0
        n = 0   
        k = 0
        #We find even subpalindriomes end make array pld2.    
        while n < size:
            k = (0 if n > j else min(pld2[i+j-n+1], j - n + 1))
            #Search for subpalindromes
            while (n + k < size) and (n - k - 1 >= 0) and (s[n+k] == s[n-k-1]):
                k += 1
            pld2[n] = k 
            if n + k - 1 > j:
                i = n - k
                j = n + k - 1
            if pld2[n] > mx2:
                mx2 = pld2[n]
                index2 = n 
            n += 1
        #print(pld1)       
        #print(pld2)
        # Return max of subpalindriomes
        if len(s[(index1 - mx1):index1+mx1+1]) > len(s[(index2 - mx2):index2+mx2]):
            return(s[(index1 - mx1):index1+mx1+1])
        else:
            return(s[(index2 - mx2):index2+mx2])


# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Example 3:

# Input: s = "a"
# Output: "a"

# Example 4:

# Input: s = "ac"
# Output: "a"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters (lower-case and/or upper-case),

