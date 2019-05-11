# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-09 21:57:09
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-10 00:29:44


# 位运算
class Solution:
	def divide(self, dividend, divisor):
		if dividend == 0:
			return 0
		if dividend > 0 and divisor > 0:
			sig = 1
		if dividend < 0 and divisor < 0:
			sig = 1
		if dividend > 0 and divisor < 0:
			sig = -1 
		if dividend < 0 and divisor > 0:
			sig = -1

		dividend = abs(dividend)
		divisor = abs(divisor)
		if dividend == 0:
			return 0

		# 防止溢出
		if divisor == 1:
			if dividend * sig > 2 ** 31 - 1:
				return 2 ** 31 - 1
			if dividend * sig < -1 * 2 ** 31:
				return -1 * 2 ** 31
			return dividend * sig

		quotient = 0
		
		while dividend >= divisor:
			tmp, times = divisor, 1
			while dividend >= tmp << 1:
				tmp <<= 1
				times <<= 1
			dividend -= tmp
			quotient += times

		return sig * quotient