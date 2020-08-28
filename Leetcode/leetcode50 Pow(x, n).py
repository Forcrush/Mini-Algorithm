# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-31 13:17:43
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-31 13:21:54


class Solution:
	def myPow(self, x, n):

		def cnt_pow(x, n):
			if n == 0: return 1
			sqrt = cnt_pow(x, n//2)
			if n % 2 == 1:
				return sqrt*sqrt*x
			else:
				return sqrt*sqrt

		return cnt_pow(x, n) if n >= 0 else 1/cnt_pow(x, -n)