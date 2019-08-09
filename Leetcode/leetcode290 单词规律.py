# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-09 22:22:17
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-09 22:28:48


class Solution(object):
	def wordPattern(self, pattern, str):
		def decompose(array):
			dic = {}
			res = []
			for i in range(len(array)):
				if dic.get(array[i], None) == None:
					dic[array[i]] = i
					res.append(i)
				else:
					res.append(dic[array[i]])
			return res

		str = [i for i in str.split() if i]
		if decompose(pattern) == decompose(str):
			return True
		return False

		