# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-07 22:14:11
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-07 22:44:33


class Solution:
	def convertToTitle(self, n):
		res = ''
		while n:
			# 先减一才能找到对应字母
			n -= 1
			res = chr(n % 26 + 65) + res
			n //= 26
		return res