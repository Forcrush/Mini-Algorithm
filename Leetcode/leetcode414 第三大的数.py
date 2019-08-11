# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 19:22:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 19:37:51


class Solution:
	def thirdMax(self, nums):
		initialval = 0
		for i in nums:
			initialval += -abs(i)
		firstmax, secondmax, thirdmax = initialval, initialval, initialval
		for i in nums:
			if i > firstmax:
				thirdmax = secondmax
				secondmax = firstmax
				firstmax = i
			elif i < firstmax and i > secondmax:
				thirdmax = secondmax
				secondmax = i
			elif i < secondmax and i > thirdmax:
				thirdmax = i
		if thirdmax == initialval:
			if firstmax == initialval:
				return '-inf'
			else:
				return firstmax
		return thirdmax

