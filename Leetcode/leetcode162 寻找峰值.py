# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 10:27:45
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 10:35:47


class Solution:
	def findPeakElement(self, nums):

		l, r = 0, len(nums)-1
		while l < r:
			mid = (l + r) // 2
			if nums[mid] < nums[mid+1]:
				l = mid + 1
			else:
				r = mid
		return l

