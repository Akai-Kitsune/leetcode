# 7. Reverse Integer Easy
# Runtime: 28 ms, faster than 89.28% of Python3 
# online submissions for Reverse Integer.
# Memory Usage: 14.3 MB, less than 9.95% of Python3 
# online submissions for Reverse Integer.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        g = range(-2**31, 2**31-1)
        if x not in g:
            result = 0
        elif x < 0:
            result = (-1 * int(str(x)[::-1][:-1]))
        else:
            result = (int(str(x)[::-1]))
        return result if result in g else 0


# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21

# Example 4:

# Input: x = 0
# Output: 0

 

# Constraints:

#     -231 <= x <= 231 - 1