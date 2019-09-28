# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-27 23:34:02
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-27 23:39:40


class Solution:
	def longestPalindrome(self, s):
		dic = {}
		for i in s:
			dic[i] = dic.get(i, 0) + 1

		res = 0
		flag = False
		for key,val in dic.items():
			if val % 2 == 0:
				res += val
			else:
				if val > 2:
					res += val - 1
				flag = True
		if flag:
			return res + 1
		else:
			return res

