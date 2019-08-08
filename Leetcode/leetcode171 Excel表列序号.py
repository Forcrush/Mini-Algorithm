# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-07 22:05:22
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-07 22:13:40


class Solution:
	def titleToNumber(self, s):
		# A - 65   Z - 90
		if s == '':
			return 0
		res = 0
		for i in range(len(s)):
			res += pow(26, len(s)-1-i) * (ord(s[i])-64)
		return res

		