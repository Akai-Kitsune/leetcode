# 4. Median of Two Sorted Arrays Hard
# result:
# Runtime: 196 ms, faster than 5.34% of Python 
# Memory Usage: 13.6 MB, less than 48.61% of Python 

class Solution(object):

	def merge(self, nums1, nums2):
		num = []; num.extend(nums1); num.extend(nums2)
		return num

	def mergeSort(self, arr):
		size = len(arr)
		if size == 1 or size == 0:
			return arr
		left = arr[:size // 2]
		right = arr[size // 2:]
		
		self.mergeSort(left)
		self.mergeSort(right)
		sizeL = len(left)
		sizeR = len(right)
		num = [0] *(sizeL + sizeR)
		(i, j, k) = (0, 0, 0)
		while i < sizeL and j < sizeR:
			if left[i] <= right[j]:
				num[k] = left[i]
				i += 1
			elif left[i] > right[j]:
				num[k] = right[j]
				j += 1
			k += 1
		while i < sizeL:
			num[k] = left[i]
			i += 1; k += 1
		while j < sizeR:
			num[k] = right[j]
			j += 1; k += 1
		for i in range(size):
			arr[i] = num[i]
		return arr

	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		num = (nums1 + nums2)
		num = self.mergeSort(num)
		size = len(num)
		if size % 2 == 1:
		    return float(num[size/2])
		else: 
			return float(num[size//2 - 1] + num[size//2 ]) / 2


# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

 

# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106

