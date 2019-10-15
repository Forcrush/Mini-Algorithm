# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-13 11:18:12
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-13 11:25:42


class Solution:
	def hasGroupsSizeX(self, deck):

		# 最大公约数
		def gcd(x, y):
			if x == 0:
				return y
			else:
				return gcd(y%x, x)

		dic = {}
		for i in deck:
			dic[i] = dic.get(i, 0) + 1

		res = -1
		for key,val in dic.items():
			if res < 0:
				res = val
			else:
				res = gcd(res, val)
		if res >= 2:
			return True
		return False
