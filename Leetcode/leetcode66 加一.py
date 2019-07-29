# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-26 15:05:01
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-26 15:05:47


class Solution:
	def plusOne(self, digits):
		l = len(digits)
		end = l - 1
		while digits[end] + 1 == 10:
			digits[end] = 0
			end -= 1
		if end >= 0:
			digits[end] += 1
			return digits
		else:
			res = [1]
			res.extend([0]*l)
			return res