# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-14 22:55:36
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-14 23:00:03


class Solution:
	def reverseString(self, s):
		"""
		Do not return anything, modify s in-place instead.
		"""
		left, right = 0, len(s)-1
		while left <= right:
			s[left], s[right] = s[right], s[left]
			left += 1
			right -= 1

			