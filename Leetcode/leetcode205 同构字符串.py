# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-09 22:16:11
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-09 22:21:11


class Solution(object):
	def isIsomorphic(self, s, t):
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
		if decompose(s) == decompose(t):
			return True
		return False