# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-25 21:09:58
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-26 01:10:31


class Solution:
	def clumsy(self, N):

		if N == 3: return 6
		if N == 2: return 2
		if N == 1: return 1
		# n*(n-1)/(n-2)+(n-3) = 2(n-2+1/(n-2)+1)
		# - n*(n-1)/(n-2)+(n-3) = - (4+2//(n-2))
		def F(n):
			return 4 + 2 // (n - 2)

		# 结果可以看成F(n) - F(n-4) - F(n-8)

		num = N
		res = 2 * num - 2 + 2 // (num - 2)
		num -= 4
		while num >= 4:
			res -= F(num)
			num -= 4
		if num == 3:
			res -= 6
		elif num == 2:
			res -= 2
		elif num == 1:
			res -= 1
		return res

